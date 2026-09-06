import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from datetime import timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("triage", ROOT / "src" / "triage.py")
assert spec and spec.loader
triage = importlib.util.module_from_spec(spec)
spec.loader.exec_module(triage)


class TriageTests(unittest.TestCase):
    def setUp(self):
        self.events = triage.load_events(ROOT / "data" / "auth_events.csv")
        self.bob = [e.copy() for e in self.events if e["user"] == "bob"]
        self.carol = [e.copy() for e in self.events if e["user"] == "carol"]
        self.dana = [e.copy() for e in self.events if e["user"] == "dana"]

    def test_demo_has_exactly_three_findings(self):
        self.assertEqual([e["user"] for e in triage.run_triage(self.events)], ["carol", "bob", "dana"])

    def test_mfa_denials_are_not_password_failures(self):
        self.assertEqual(triage.detect_bruteforce(self.carol), [])

    def test_clean_user_has_no_alert(self):
        self.assertNotIn("alice", [e["user"] for e in triage.run_triage(self.events)])

    def test_unsorted_input_is_stable(self):
        self.assertEqual(triage.run_triage(self.events[::-1]), triage.run_triage(self.events))

    def test_below_threshold(self):
        self.assertEqual(triage.detect_bruteforce(self.bob[1:]), [])

    def test_window_boundary_inclusive(self):
        self.bob[-1]["timestamp"] = "2026-08-20T13:10:00Z"
        self.assertEqual(len(triage.detect_bruteforce(self.bob)), 1)

    def test_window_boundary_outside(self):
        self.bob[-1]["timestamp"] = "2026-08-20T13:10:01Z"
        self.assertEqual(triage.detect_bruteforce(self.bob), [])

    def test_failures_need_same_source_ip(self):
        self.bob[-1]["source_ip"] = "192.0.2.10"
        self.assertEqual(triage.detect_bruteforce(self.bob), [])

    def test_success_must_follow_failures(self):
        self.bob[-1]["timestamp"] = "2026-08-20T12:59:00Z"
        self.assertEqual(triage.detect_bruteforce(self.bob), [])

    def test_equal_times_do_not_prove_order(self):
        for event in self.bob:
            event["timestamp"] = "2026-08-20T13:00:00Z"
        self.assertEqual(triage.detect_bruteforce(self.bob), [])

    def test_failures_not_recycled_after_success(self):
        next_success = dict(self.bob[-1], timestamp="2026-08-20T13:06:00Z")
        self.assertEqual(len(triage.detect_bruteforce(self.bob + [next_success])), 1)

    def test_duplicate_rows_do_not_inflate_count(self):
        self.assertEqual(triage.detect_bruteforce([self.bob[0]] * 5 + [self.bob[-1]]), [])

    def test_mfa_requires_explicit_approval(self):
        self.carol[-1]["mfa_result"] = "not_applicable"
        self.assertEqual(triage.detect_mfa_fatigue(self.carol), [])

    def test_mfa_timeouts_supported(self):
        for event in self.carol[:-1]:
            event["mfa_result"] = "timeout"
        self.assertEqual(len(triage.detect_mfa_fatigue(self.carol)), 1)

    def test_mfa_can_span_ips(self):
        self.carol[-1]["source_ip"] = "192.0.2.99"
        self.assertEqual(len(triage.detect_mfa_fatigue(self.carol)), 1)

    def test_unknown_city_not_guessed(self):
        self.dana[-1]["city"] = "Unknown"
        self.assertEqual(triage.detect_impossible_travel(self.dana), [])

    def test_simultaneous_distant_logins_flagged(self):
        self.dana[-1]["timestamp"] = self.dana[0]["timestamp"]
        self.assertEqual(len(triage.detect_impossible_travel(self.dana)), 1)

    def test_plausible_travel_not_flagged(self):
        self.dana[-1]["timestamp"] = "2026-08-22T15:00:00Z"
        self.assertEqual(triage.detect_impossible_travel(self.dana), [])

    def test_naive_time_rejected(self):
        with self.assertRaises(ValueError):
            triage.parse_ts("2026-08-20T13:00:00")

    def test_timezone_normalized(self):
        self.assertEqual(triage.parse_ts("2026-08-20T09:00:00-04:00"), triage.parse_ts("2026-08-20T13:00:00Z"))

    def test_bad_ip_rejected(self):
        self.bob[0]["source_ip"] = "999.1.1.1"
        with self.assertRaises(ValueError):
            triage.run_triage(self.bob)

    def test_missing_field_rejected(self):
        del self.bob[0]["user"]
        with self.assertRaises(ValueError):
            triage.run_triage(self.bob)

    def test_bad_result_rejected(self):
        self.bob[0]["result"] = "maybe"
        with self.assertRaises(ValueError):
            triage.run_triage(self.bob)

    def test_inconsistent_mfa_rejected(self):
        self.carol[-1]["mfa_result"] = "denied"
        with self.assertRaises(ValueError):
            triage.run_triage(self.carol)

    def test_invalid_threshold_rejected(self):
        with self.assertRaises(ValueError):
            triage.run_triage(self.events, min_count=0)

    def test_empty_input(self):
        self.assertEqual(triage.run_triage([]), [])

    def test_json_cli(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = triage.main([str(ROOT / "data" / "auth_events.csv"), "--json"])
        self.assertEqual(code, 0)
        self.assertEqual(len(json.loads(output.getvalue())), 3)

    def test_missing_file_has_clean_error(self):
        with contextlib.redirect_stderr(io.StringIO()):
            code = triage.main([str(ROOT / "missing.csv")])
        self.assertEqual(code, 2)

    def test_csv_header_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "bad.csv"
            path.write_text("wrong,header\na,b\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                triage.load_events(path)

    def test_haversine_identical_points(self):
        self.assertAlmostEqual(triage.haversine_km((43, -79), (43, -79)), 0)


if __name__ == "__main__":
    unittest.main()
