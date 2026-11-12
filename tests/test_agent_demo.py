import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from agent_demo import run_demo

class ContractTests(unittest.TestCase):
    def run_case(self, request, scenario="ready"):
        return run_demo(request, scenario, {"desk"})

    def test_valid_goal_is_explicitly_mock(self):
        r = self.run_case({"intent": "navigate", "landmark_id": "desk"})
        self.assertEqual(r["status"], "ARRIVED")
        self.assertTrue(r["demo_only"])
        self.assertEqual(r["navigation_backend"], "mock")

    def test_unknown_landmark_never_dispatches(self):
        r = self.run_case({"intent": "navigate", "landmark_id": "invented"})
        self.assertEqual(r["status"], "REJECTED")
        self.assertFalse(r["goal_sent"])

    def test_arbitrary_coordinate_is_rejected(self):
        r = self.run_case({"intent": "navigate", "landmark_id": "desk", "x": 100})
        self.assertEqual(r["status"], "REJECTED")
        self.assertFalse(r["goal_sent"])

    def test_bad_schema_types_are_rejected(self):
        for request in ([], {}, {"intent": []}, {"intent":"navigate","landmark_id":[]}):
            with self.subTest(request=request):
                self.assertEqual(self.run_case(request)["status"], "REJECTED")

    def test_stale_or_blocked_does_not_dispatch(self):
        for scenario, expected in (("stale", "NOT_READY"), ("blocked", "NO_PATH"), ("busy", "BUSY")):
            with self.subTest(scenario=scenario):
                r = self.run_case({"intent":"navigate","landmark_id":"desk"}, scenario)
                self.assertEqual(r["status"], expected)
                self.assertFalse(r["goal_sent"])

    def test_clarify_does_not_dispatch(self):
        r = self.run_case({"intent":"clarify","question":"哪個門口？"})
        self.assertEqual(r["status"], "CLARIFY")
        self.assertFalse(r["goal_sent"])

    def test_failure_and_timeout_are_not_success(self):
        for scenario in ("failed", "timeout"):
            with self.subTest(scenario=scenario):
                r = self.run_case({"intent":"navigate","landmark_id":"desk"}, scenario)
                self.assertNotEqual(r["status"], "ARRIVED")

    def test_cancel_does_not_claim_real_stop(self):
        r = self.run_case({"intent":"cancel"}, "busy")
        self.assertEqual(r["status"], "CANCELED")
        self.assertFalse(r["goal_sent"])
        self.assertFalse(r["stop_confirmed"])

    def test_empty_question_is_rejected(self):
        self.assertEqual(self.run_case({"intent":"clarify","question":" "})["status"], "REJECTED")

if __name__ == "__main__":
    unittest.main()
