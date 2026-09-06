import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "src" / "triage.py"
spec = importlib.util.spec_from_file_location("triage", MODULE_PATH)
triage = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(triage)


class TriageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.events = triage.load_events(ROOT / "data" / "auth_events.csv")

    def test_bruteforce_detection(self):
        findings = triage.detect_bruteforce(self.events)
        self.assertTrue(any(f["user"] == "bob" for f in findings))

    def test_mfa_fatigue_detection(self):
        findings = triage.detect_mfa_fatigue(self.events)
        self.assertTrue(any(f["user"] == "carol" for f in findings))

    def test_impossible_travel_detection(self):
        findings = triage.detect_impossible_travel(self.events)
        self.assertTrue(any(f["user"] == "dana" for f in findings))

    def test_clean_user_not_flagged(self):
        findings = triage.run_triage(self.events)
        self.assertFalse(any(f["user"] == "alice" for f in findings))


if __name__ == "__main__":
    unittest.main()
