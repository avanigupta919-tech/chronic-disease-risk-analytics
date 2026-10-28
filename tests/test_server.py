"""
Automated Integration & Unit Test Suite
Verifies:
- API overview endpoint
- HTML route responses (200 OK)
- Triage roster search & filter
- Clinical AI Risk Assessment Agent POST calculations
"""

import os
import sys
import json
import time
import subprocess
import urllib.request

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
run_py = os.path.join(base_dir, "run.py")
python_exe = sys.executable

def run_tests():
    print("[*] Starting web server for integration testing on port 5058...")
    proc = subprocess.Popen([python_exe, run_py, "5058"], cwd=base_dir)
    try:
        time.sleep(2.5)

        # 1. Test /api/overview
        with urllib.request.urlopen("http://localhost:5058/api/overview") as resp:
            assert resp.status == 200
            data = json.loads(resp.read().decode("utf-8"))
            assert data["total_patients"] == 6000
            print("[PASS] GET /api/overview - Ingested 6,000 records verified.")

        # 2. Test Home Page
        with urllib.request.urlopen("http://localhost:5058/") as resp:
            assert resp.status == 200
            print("[PASS] GET / - Executive overview rendered successfully.")

        # 3. Test Clinical Officer Page
        with urllib.request.urlopen("http://localhost:5058/clinical-officer") as resp:
            assert resp.status == 200
            print("[PASS] GET /clinical-officer - Dr. Michael Carter dashboard rendered.")

        # 4. Test Lifestyle Analyst Page
        with urllib.request.urlopen("http://localhost:5058/data-analyst") as resp:
            assert resp.status == 200
            print("[PASS] GET /data-analyst - Emily Rodriguez dashboard rendered.")

        # 5. Test Public Health Page
        with urllib.request.urlopen("http://localhost:5058/public-health") as resp:
            assert resp.status == 200
            print("[PASS] GET /public-health - Dr. Priya Nair dashboard rendered.")

        # 6. Test Tableau Story Page
        with urllib.request.urlopen("http://localhost:5058/tableau-story") as resp:
            assert resp.status == 200
            print("[PASS] GET /tableau-story - 5-scene clinical story rendered.")

        # 7. Test Clinical AI Risk Agent POST endpoint
        payload = {
            "age": 65,
            "systolic_bp": 172,
            "diastolic_bp": 102,
            "total_cholesterol": 270,
            "fasting_glucose": 195,
            "bmi": 34.8,
            "smoking_habit": "Current Daily",
            "alcohol_consumption": "Heavy",
            "exercise_level": "Sedentary",
            "diet_quality": "Poor",
            "chest_pain_symptoms": "Typical Angina / Severe"
        }
        req = urllib.request.Request(
            "http://localhost:5058/api/assess-risk",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req) as resp:
            assert resp.status == 200
            res = json.loads(resp.read().decode("utf-8"))
            assert res["risk_tier"] == "Critical / Urgent"
            assert res["overall_risk_score"] > 70.0
            print(f"[PASS] POST /api/assess-risk - Agent evaluated tier '{res['risk_tier']}' with score {res['overall_risk_score']}.")

        print("\nAll integration tests passed successfully (100% SLA)!\n")
    finally:
        proc.terminate()
        proc.kill()

if __name__ == "__main__":
    run_tests()
