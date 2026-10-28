"""
Data Preparation & Feature Engineering Pipeline
Performs:
1. Data Ingestion & Quality Validation
2. Feature Transformation & Categorization (Age Groups, BMI Categories, BP Stages, Glucose/Cholesterol Bins)
3. Advanced Clinical Feature Engineering (Cardiovascular Flags, Metabolic Syndrome, Lifestyle Risk Index)
4. Exports Processed Data for Tableau Desktop, SQLite Database, and Flask Analytics Engine
"""

import os
import sqlite3
import pandas as pd
import numpy as np

def categorize_age(age):
    if age < 35:
        return "18-34 Young Adult"
    elif age < 50:
        return "35-49 Middle Age"
    elif age < 65:
        return "50-64 Older Adult"
    else:
        return "65+ Senior"

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight (<18.5)"
    elif bmi < 25.0:
        return "Normal Weight (18.5-24.9)"
    elif bmi < 30.0:
        return "Overweight (25.0-29.9)"
    elif bmi < 35.0:
        return "Obesity Class I (30.0-34.9)"
    else:
        return "Obesity Class II/III (>=35.0)"

def categorize_bp(sbp, dbp):
    if sbp >= 180 or dbp >= 120:
        return "Hypertensive Crisis"
    elif sbp >= 140 or dbp >= 90:
        return "Hypertension Stage 2"
    elif sbp >= 130 or dbp >= 80:
        return "Hypertension Stage 1"
    elif sbp >= 120 and dbp < 80:
        return "Elevated"
    else:
        return "Normal"

def categorize_cholesterol(chol):
    if chol < 200:
        return "Desirable (<200 mg/dL)"
    elif chol < 240:
        return "Borderline High (200-239 mg/dL)"
    else:
        return "High Risk (>=240 mg/dL)"

def categorize_glucose(glucose):
    if glucose < 100:
        return "Normal (<100 mg/dL)"
    elif glucose < 126:
        return "Prediabetic (100-125 mg/dL)"
    else:
        return "Diabetic (>=126 mg/dL)"

def calculate_lifestyle_risk_index(row):
    score = 0
    # Smoking
    if row["smoking_habit"] == "Current Daily": score += 3
    elif row["smoking_habit"] == "Current Occasional": score += 2
    elif row["smoking_habit"] == "Former": score += 1
    
    # Alcohol
    if row["alcohol_consumption"] == "Heavy": score += 3
    elif row["alcohol_consumption"] == "Moderate": score += 1
    
    # Exercise
    if row["exercise_level"] == "Sedentary": score += 3
    elif row["exercise_level"] == "Light": score += 2
    elif row["exercise_level"] == "Moderate": score += 1
    
    # Diet
    if row["diet_quality"] == "Poor": score += 3
    elif row["diet_quality"] == "Average": score += 1
    
    if score >= 8: return "High Lifestyle Risk"
    elif score >= 4: return "Moderate Lifestyle Risk"
    else: return "Low Lifestyle Risk"

def calculate_symptom_severity(row):
    score = 0
    if row["chest_pain_symptoms"] in ["Typical Angina / Severe", "Exertional / Discomfort"]: score += 3
    elif row["chest_pain_symptoms"] == "Atypical": score += 1
    
    if row["fatigue_condition"] == "Chronic/Severe": score += 2
    elif row["fatigue_condition"] == "Frequent": score += 1
    
    if row["dizziness_patterns"] == "Frequent/Persistent": score += 2
    elif row["dizziness_patterns"] in ["Positional", "Occasional"]: score += 1
    
    if score >= 5: return "Severe Symptoms"
    elif score >= 2: return "Moderate Symptoms"
    elif score >= 1: return "Mild Symptoms"
    else: return "Asymptomatic"

def process_data(raw_csv_path, output_dir):
    print(f"Reading raw data from: {raw_csv_path}")
    df = pd.read_csv(raw_csv_path)
    print(f"Total records ingested: {len(df)}")
    
    # 1. Feature Engineering: Demographic & Clinical Bins
    df["age_group"] = df["age"].apply(categorize_age)
    df["bmi_category"] = df["bmi"].apply(categorize_bmi)
    df["bp_category"] = df.apply(lambda r: categorize_bp(r["systolic_bp"], r["diastolic_bp"]), axis=1)
    df["cholesterol_category"] = df["total_cholesterol"].apply(categorize_cholesterol)
    df["glucose_category"] = df["fasting_glucose"].apply(categorize_glucose)
    
    # 2. Behavioral & Symptom Scores
    df["lifestyle_risk_tier"] = df.apply(calculate_lifestyle_risk_index, axis=1)
    df["symptom_severity_tier"] = df.apply(calculate_symptom_severity, axis=1)
    
    # 3. Clinical Warning Flags
    df["cardiovascular_warning"] = (
        (df["systolic_bp"] >= 140) | 
        (df["total_cholesterol"] >= 240) | 
        (df["chest_pain_symptoms"].isin(["Typical Angina / Severe", "Exertional / Discomfort"])) |
        (df["heart_disease"] == 1)
    ).astype(int)
    
    df["metabolic_syndrome_flag"] = (
        (df["bmi"] >= 30.0) & 
        (df["fasting_glucose"] >= 100) & 
        (df["systolic_bp"] >= 130)
    ).astype(int)
    
    df["stroke_vulnerability_index"] = (
        (df["systolic_bp"] >= 150).astype(int) * 3 +
        (df["smoking_habit"] == "Current Daily").astype(int) * 2 +
        (df["alcohol_consumption"] == "Heavy").astype(int) * 2 +
        (df["age"] >= 60).astype(int) * 2 +
        (df["heart_disease"] == 1).astype(int) * 2 +
        (df["dizziness_patterns"] == "Frequent/Persistent").astype(int) * 2
    )
    
    # 4. Disease Profile Summary String (for quick clinical review)
    def disease_summary(r):
        diseases = []
        if r["heart_disease"]: diseases.append("Heart Disease")
        if r["diabetes"]: diseases.append("Diabetes")
        if r["stroke"]: diseases.append("Stroke")
        if r["kidney_disease"]: diseases.append("CKD")
        return ", ".join(diseases) if diseases else "None Diagnosed"
    
    df["diagnosed_conditions"] = df.apply(disease_summary, axis=1)
    
    # Save processed outputs
    processed_dir = os.path.join(output_dir, "data", "processed")
    tableau_dir = os.path.join(output_dir, "data", "tableau")
    os.makedirs(processed_dir, exist_ok=True)
    os.makedirs(tableau_dir, exist_ok=True)
    
    processed_csv = os.path.join(processed_dir, "chronic_disease_cleaned.csv")
    tableau_csv = os.path.join(tableau_dir, "tableau_dataset.csv")
    sqlite_path = os.path.join(processed_dir, "chronic_disease_analytics.db")
    
    df.to_csv(processed_csv, index=False)
    df.to_csv(tableau_csv, index=False)
    print(f"[OK] Cleaned CSV exported: {processed_csv}")
    print(f"[OK] Tableau-ready CSV exported: {tableau_csv}")
    
    # Save to SQLite Database
    conn = sqlite3.connect(sqlite_path)
    df.to_sql("chronic_disease_patients", conn, if_exists="replace", index=False)
    
    # Create indexes for high-performance Tableau database queries
    cur = conn.cursor()
    cur.execute("CREATE INDEX IF NOT EXISTS idx_risk_tier ON chronic_disease_patients(risk_tier);")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_age_group ON chronic_disease_patients(age_group);")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_conditions ON chronic_disease_patients(heart_disease, diabetes, stroke);")
    conn.commit()
    conn.close()
    print(f"[OK] Indexed SQLite Analytics Database created: {sqlite_path}")
    
    return df

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    raw_path = os.path.join(project_root, "data", "raw", "chronic_disease_raw.csv")
    
    if not os.path.exists(raw_path):
        print("Raw dataset not found. Generating now...")
        from generate_dataset import generate_patient_data, save_to_database_and_csv
        df_raw = generate_patient_data(6000)
        save_to_database_and_csv(df_raw, project_root)
        
    process_data(raw_path, project_root)
    print("Data preparation and feature engineering pipeline finished successfully.")
