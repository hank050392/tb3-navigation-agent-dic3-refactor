"""Offline contract demonstration. No LLM, ROS, sensors, or robot control."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ("ready", "stale", "blocked", "failed", "timeout", "busy")

def validate_request(request, landmark_ids):
    if not isinstance(request, dict):
        return "request must be an object"
    intent = request.get("intent")
    schemas = {"navigate": {"intent", "landmark_id"}, "cancel": {"intent"},
               "clarify": {"intent", "question"}, "reject": {"intent", "reason"}}
    if not isinstance(intent, str) or intent not in schemas:
        return "unknown intent"
    if set(request) != schemas[intent]:
        return "missing or extra fields"
    if intent == "navigate":
        target = request["landmark_id"]
        if not isinstance(target, str) or target not in landmark_ids:
            return "unknown landmark"
    for field in ("question", "reason"):
        if field in request and (not isinstance(request[field], str) or not request[field].strip()):
            return "empty or invalid " + field
    return None

def run_demo(request, scenario="ready", landmark_ids=None):
    if scenario not in SCENARIOS:
        raise ValueError("unknown mock scenario")
    if landmark_ids is None:
        landmark_ids = set(json.loads((ROOT / "config/landmarks.json").read_text())["landmarks"])
    output = {"demo_only": True, "navigation_backend": "mock",
              "timestamp": datetime.now(timezone.utc).isoformat(), "goal_sent": False,
              "evidence": [{"source": "mock_scenario", "value": scenario}]}
    error = validate_request(request, landmark_ids)
    if error:
        return {**output, "status": "REJECTED", "reason": error}
    intent = request["intent"]
    if intent == "cancel":
        return {**output, "status": "CANCELED", "reason": "mock cancellation only",
                "stop_confirmed": False}
    if intent == "clarify":
        return {**output, "status": "CLARIFY", "question": request["question"]}
    if intent == "reject":
        return {**output, "status": "REJECTED", "reason": request["reason"]}
    if scenario == "busy":
        return {**output, "status": "BUSY", "reason": "mock active mission"}
    if scenario == "stale":
        return {**output, "status": "NOT_READY", "reason": "mock stale sensor data"}
    if scenario == "blocked":
        return {**output, "status": "NO_PATH", "reason": "mock path check failed"}
    results = {"ready": "ARRIVED", "failed": "FAILED", "timeout": "TIMEOUT"}
    output["evidence"].append({"source": "mock_navigation_result", "value": results[scenario]})
    return {**output, "goal_sent": True, "landmark_id": request["landmark_id"],
            "status": results[scenario], "reason": "simulated outcome; no physical motion"}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--scenario", choices=SCENARIOS, default="ready")
    args = parser.parse_args()
    try:
        request = json.loads(args.request.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    print(json.dumps(run_demo(request, args.scenario), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
