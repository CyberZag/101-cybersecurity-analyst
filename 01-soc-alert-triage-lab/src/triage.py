"""Offline authentication triage over synthetic CSV data; not a production SIEM."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict, deque
from datetime import datetime, timezone
from ipaddress import ip_address
from math import asin, cos, radians, sin, sqrt
from pathlib import Path

FIELDS = ("timestamp", "user", "source_ip", "country", "city", "device", "result", "mfa_result")
CITY_COORDS = {
    ("Canada", "Toronto"): (43.6532, -79.3832),
    ("Canada", "Vancouver"): (49.2827, -123.1207),
    ("Germany", "Berlin"): (52.5200, 13.4050),
    ("Japan", "Tokyo"): (35.6762, 139.6503),
}
Event = dict[str, str]


def parse_ts(value: str) -> datetime:
    """Reject timezone-free timestamps instead of assuming the machine's timezone."""
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        raise ValueError("timestamp must include Z or a UTC offset")
    return dt.astimezone(timezone.utc)


def normalize(events: list[Event]) -> list[Event]:
    """Validate, normalize UTC, remove exact duplicate rows, and sort."""
    unique: dict[tuple[str, ...], Event] = {}
    for row_number, raw in enumerate(events, 2):
        try:
            event = {key: str(raw[key]).strip() for key in FIELDS if raw.get(key) is not None}
            if len(event) != len(FIELDS) or any(not value for value in event.values()):
                raise ValueError("missing or empty required field")
            event["timestamp"] = parse_ts(event["timestamp"]).isoformat()
            event["source_ip"] = str(ip_address(event["source_ip"]))
            if event["result"] not in {"success", "failed"}:
                raise ValueError("result must be success or failed")
            if event["mfa_result"] not in {"approved", "denied", "timeout", "not_applicable"}:
                raise ValueError("unrecognized mfa_result")
            if event["result"] == "success" and event["mfa_result"] in {"denied", "timeout"}:
                raise ValueError("success cannot also contain an MFA denial or timeout")
            if event["result"] == "failed" and event["mfa_result"] == "approved":
                raise ValueError("this simplified schema cannot represent failure after MFA approval")
        except (KeyError, ValueError, TypeError) as exc:
            raise ValueError(f"row {row_number}: {exc}") from exc
        unique[tuple(event[key] for key in FIELDS)] = event
    return sorted(unique.values(), key=lambda e: parse_ts(e["timestamp"]))


def load_events(path: str | Path) -> list[Event]:
    with open(path, newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not set(FIELDS).issubset(reader.fieldnames):
            raise ValueError("CSV header must include: " + ", ".join(FIELDS))
        rows = list(reader)
        if any(None in row for row in rows):
            raise ValueError("CSV row has more values than the header")
    return normalize(rows)


def _sequences(events: list[Event], mfa: bool, min_count: int, window_seconds: int) -> list[dict]:
    if min_count < 1 or window_seconds < 1:
        raise ValueError("threshold and time window must be positive")
    pending: dict[tuple, deque] = defaultdict(deque)
    findings = []
    for event in normalize(events):
        now = parse_ts(event["timestamp"])
        # MFA bursts may rotate IPs; non-MFA failures must share user AND IP.
        key = (event["user"],) if mfa else (event["user"], event["source_ip"])
        history = pending[key]
        while history and (now - history[0][0]).total_seconds() > window_seconds:
            history.popleft()
        if event["result"] == "failed":
            qualifies = event["mfa_result"] in {"denied", "timeout"} if mfa else event["mfa_result"] == "not_applicable"
            if qualifies:
                history.append((now, event))
            continue
        # Equal timestamps do not establish that a failure preceded success.
        preceding = [entry for timestamp, entry in history if timestamp < now]
        approval_ok = not mfa or event["mfa_result"] == "approved"
        if len(preceding) >= min_count and approval_ok:
            findings.append({
                "type": "MFA fatigue candidate" if mfa else "Brute-force candidate",
                "severity": "HIGH", "score": 85 if mfa else 80,
                "user": event["user"], "source_ip": event["source_ip"],
                "first_seen": preceding[0]["timestamp"], "last_seen": event["timestamp"],
                "count": len(preceding),
                "evidence": f"{len(preceding)} {'MFA denials/timeouts' if mfa else 'non-MFA failures'} in {window_seconds}s before {'MFA-approved ' if mfa else ''}success",
                "mitre": "T1621; T1078 (hypothesis)" if mfa else "T1110; T1078 (hypothesis)",
            })
        # A success ends this sequence; do not recycle failures for later successes.
        history.clear()
    return findings


def detect_bruteforce(events: list[Event], min_count: int = 5, window_seconds: int = 600) -> list[dict]:
    return _sequences(events, False, min_count, window_seconds)


def detect_mfa_fatigue(events: list[Event], min_count: int = 5, window_seconds: int = 600) -> list[dict]:
    return _sequences(events, True, min_count, window_seconds)


def haversine_km(a: tuple[float, float], b: tuple[float, float]) -> float:
    lat1, lon1 = map(radians, a)
    lat2, lon2 = map(radians, b)
    h = sin((lat2 - lat1) / 2) ** 2 + cos(lat1) * cos(lat2) * sin((lon2 - lon1) / 2) ** 2
    return 6371.0 * 2 * asin(sqrt(min(1.0, max(0.0, h))))


def detect_impossible_travel(events: list[Event]) -> list[dict]:
    previous: dict[str, Event] = {}
    findings = []
    for second in normalize(events):
        if second["result"] != "success":
            continue
        first = previous.get(second["user"])
        previous[second["user"]] = second
        if first is None:
            continue
        a = CITY_COORDS.get((first["country"], first["city"]))
        b = CITY_COORDS.get((second["country"], second["city"]))
        if a is None or b is None:
            continue  # Unknown location is NOT evidence of safety.
        seconds = (parse_ts(second["timestamp"]) - parse_ts(first["timestamp"])).total_seconds()
        km = haversine_km(a, b)
        if km > 500 and (seconds == 0 or km / (seconds / 3600) > 900):
            detail = "simultaneous timestamps" if seconds == 0 else f"{km / (seconds / 3600):.0f} km/h"
            findings.append({
                "type": "Suspicious geo-velocity", "severity": "MEDIUM", "score": 60,
                "user": second["user"], "source_ip": second["source_ip"],
                "first_seen": first["timestamp"], "last_seen": second["timestamp"], "count": 2,
                "evidence": f"{km:.0f} km in {seconds / 60:.1f} minutes; {detail}; validate VPN/device context",
                "mitre": "T1078 (hypothesis, not proof of compromise)",
            })
    return findings


def run_triage(events: list[Event], min_count: int = 5, window_seconds: int = 600) -> list[dict]:
    findings = detect_bruteforce(events, min_count, window_seconds)
    findings += detect_mfa_fatigue(events, min_count, window_seconds)
    findings += detect_impossible_travel(events)
    return sorted(findings, key=lambda item: (-item["score"], item["last_seen"], item["user"]))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--json", action="store_true", help="print structured findings as JSON")
    parser.add_argument("--min-count", type=int, default=5)
    parser.add_argument("--window-seconds", type=int, default=600)
    args = parser.parse_args(argv)
    try:
        findings = run_triage(load_events(args.csv_path), args.min_count, args.window_seconds)
    except (OSError, UnicodeError, ValueError, csv.Error) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(findings, indent=2))
    else:
        for finding in findings:
            print(f"{finding['severity']} | {finding['user']} | {finding['type']} | {finding['evidence']}")
        print(f"{len(findings)} finding(s). Synthetic lab only; investigate before containment.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
