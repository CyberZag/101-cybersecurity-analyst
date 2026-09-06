from __future__ import annotations

import csv
import sys
from collections import defaultdict
from datetime import datetime, timezone
from math import asin, cos, radians, sin, sqrt
from pathlib import Path

CITY_COORDS = {
    ("Canada", "Toronto"): (43.6532, -79.3832),
    ("Canada", "Vancouver"): (49.2827, -123.1207),
    ("Germany", "Berlin"): (52.5200, 13.4050),
    ("Japan", "Tokyo"): (35.6762, 139.6503),
}


def parse_ts(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def haversine_km(a: tuple[float, float], b: tuple[float, float]) -> float:
    lat1, lon1 = map(radians, a)
    lat2, lon2 = map(radians, b)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    h = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return 6371.0 * 2 * asin(sqrt(h))


def load_events(path: str | Path) -> list[dict[str, str]]:
    with open(path, newline="", encoding="utf-8") as f:
        events = list(csv.DictReader(f))
    return sorted(events, key=lambda e: parse_ts(e["timestamp"]))


def detect_bruteforce(events: list[dict[str, str]]) -> list[dict]:
    findings = []
    by_user: dict[str, list[dict[str, str]]] = defaultdict(list)
    for e in events:
        by_user[e["user"]].append(e)

    for user, timeline in by_user.items():
        for idx, event in enumerate(timeline):
            if event["result"] != "success":
                continue
            success_time = parse_ts(event["timestamp"])
            failures = [
                prev
                for prev in timeline[:idx]
                if prev["result"] == "failed"
                and 0 <= (success_time - parse_ts(prev["timestamp"])).total_seconds() <= 600
                and prev["source_ip"] == event["source_ip"]
            ]
            if len(failures) >= 5:
                findings.append({
                    "type": "Brute force followed by success",
                    "severity": "HIGH",
                    "score": 80,
                    "user": user,
                    "source_ip": event["source_ip"],
                    "evidence": f"{len(failures)} failures within 10 minutes before successful sign-in",
                    "mitre": "T1110 + T1078",
                })
    return findings


def detect_mfa_fatigue(events: list[dict[str, str]]) -> list[dict]:
    findings = []
    by_user: dict[str, list[dict[str, str]]] = defaultdict(list)
    for e in events:
        by_user[e["user"]].append(e)

    for user, timeline in by_user.items():
        for idx, event in enumerate(timeline):
            if event["result"] != "success":
                continue
            success_time = parse_ts(event["timestamp"])
            denied = [
                prev
                for prev in timeline[:idx]
                if prev["mfa_result"] == "denied"
                and 0 <= (success_time - parse_ts(prev["timestamp"])).total_seconds() <= 600
            ]
            if len(denied) >= 5:
                findings.append({
                    "type": "MFA fatigue followed by success",
                    "severity": "CRITICAL",
                    "score": 95,
                    "user": user,
                    "source_ip": event["source_ip"],
                    "evidence": f"{len(denied)} denied MFA prompts within 10 minutes before approval",
                    "mitre": "T1621 + T1078",
                })
    return findings


def detect_impossible_travel(events: list[dict[str, str]]) -> list[dict]:
    findings = []
    by_user: dict[str, list[dict[str, str]]] = defaultdict(list)
    for e in events:
        if e["result"] == "success":
            by_user[e["user"]].append(e)

    for user, timeline in by_user.items():
        for first, second in zip(timeline, timeline[1:]):
            p1 = CITY_COORDS.get((first["country"], first["city"]))
            p2 = CITY_COORDS.get((second["country"], second["city"]))
            if not p1 or not p2:
                continue
            hours = (parse_ts(second["timestamp"]) - parse_ts(first["timestamp"])).total_seconds() / 3600
            if hours <= 0:
                continue
            distance = haversine_km(p1, p2)
            speed = distance / hours
            if distance > 500 and speed > 900:
                findings.append({
                    "type": "Impossible travel",
                    "severity": "CRITICAL",
                    "score": 90,
                    "user": user,
                    "source_ip": second["source_ip"],
                    "evidence": f"{distance:.0f} km in {hours:.2f} hours ({speed:.0f} km/h)",
                    "mitre": "T1078",
                })
    return findings


def run_triage(events: list[dict[str, str]]) -> list[dict]:
    findings = detect_bruteforce(events) + detect_mfa_fatigue(events) + detect_impossible_travel(events)
    return sorted(findings, key=lambda f: f["score"], reverse=True)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python triage.py <auth_events.csv>")
        return 2
    findings = run_triage(load_events(sys.argv[1]))
    if not findings:
        print("No suspicious patterns detected.")
        return 0
    for i, finding in enumerate(findings, 1):
        print(f"[{i}] {finding['severity']} | {finding['type']}")
        print(f"    User: {finding['user']} | Source IP: {finding['source_ip']}")
        print(f"    Evidence: {finding['evidence']}")
        print(f"    MITRE ATT&CK: {finding['mitre']}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
