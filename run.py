"""
Chronic Disease Health Risk Assessment and Patient Monitoring System
Unified Application Launcher
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

def ensure_data_prepared():
    db_path = os.path.join(BASE_DIR, "data", "processed", "chronic_disease_analytics.db")
    if not os.path.exists(db_path):
        print("[*] Processing clinical dataset and creating database...")
        from scripts.data_preparation import process_data
        raw_csv = os.path.join(BASE_DIR, "data", "raw", "chronic_disease_raw.csv")
        if not os.path.exists(raw_csv):
            from scripts.generate_dataset import generate_patient_data, save_to_database_and_csv
            df = generate_patient_data(6000)
            save_to_database_and_csv(df, BASE_DIR)
        process_data(raw_csv, BASE_DIR)

    twb_path = os.path.join(BASE_DIR, "tableau", "Chronic_Disease_Risk_Analysis.twb")
    if not os.path.exists(twb_path):
        from scripts.build_tableau_workbook import generate_tableau_workbook
        generate_tableau_workbook(twb_path)

def main():
    ensure_data_prepared()
    
    port = 5000
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        port = int(sys.argv[1])

    # Check for Flask availability
    try:
        import flask
        print("\n" + "="*70)
        print(" [OK] Flask detected. Launching Flask Web Application...")
        print(f" Web Application URL: http://localhost:{port}/")
        print("="*70 + "\n")
        from app.app import app
        app.run(host="0.0.0.0", port=port, debug=False)
    except ImportError:
        print("\n" + "="*70)
        print(" [i] Flask not found in environment. Launching built-in Zero-Dependency Server...")
        print(f" Web Application URL: http://localhost:{port}/")
        print("="*70 + "\n")
        from app.standalone_server import run_server
        run_server(port)

if __name__ == "__main__":
    main()
