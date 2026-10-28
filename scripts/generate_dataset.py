"""
Data Collection & Generation Script: Chronic Disease Patient Health Records
Generates a realistic clinical dataset of 6,000 patient records modeling:
- Demographics (Age, Gender, Age Group)
- Clinical Indicators (Blood Pressure, Cholesterol, Glucose, BMI)
- Lifestyle Behaviors (Smoking, Alcohol, Exercise, Diet)
- Symptoms (Fatigue, Chest Pain, Dizziness)
- Chronic Diseases (Heart Disease, Diabetes, Stroke, Kidney Disease)
- Multi-morbidity Count, Calculated Clinical Risk Scores, and Risk Tiers
"""

import os
import random
import sqlite3
import numpy as np
import pandas as pd

def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)

def generate_patient_data(num_records=6000):
    set_seed(42)
    
    patient_ids = [f"PAT-{10000 + i}" for i in range(1, num_records + 1)]
    
    # Demographics
    ages = np.random.normal(loc=52, scale=16, size=num_records)
    ages = np.clip(ages, 18, 88).astype(int)
    
    genders = np.random.choice(["Male", "Female"], size=num_records, p=[0.49, 0.51])
    
    # Lifestyle Behaviors
    smoking_options = ["Never", "Former", "Current Occasional", "Current Daily"]
    smoking_probs = [0.50, 0.22, 0.12, 0.16]
    smoking_habits = np.random.choice(smoking_options, size=num_records, p=smoking_probs)
    
    alcohol_options = ["None", "Low", "Moderate", "Heavy"]
    alcohol_probs = [0.38, 0.32, 0.20, 0.10]
    alcohol_habits = np.random.choice(alcohol_options, size=num_records, p=alcohol_probs)
    
    exercise_options = ["Sedentary", "Light", "Moderate", "Vigorous"]
    exercise_probs = [0.35, 0.30, 0.25, 0.10]
    exercise_levels = np.random.choice(exercise_options, size=num_records, p=exercise_probs)
    
    diet_options = ["Poor", "Average", "Healthy"]
    diet_probs = [0.34, 0.44, 0.22]
    diet_qualities = np.random.choice(diet_options, size=num_records, p=diet_probs)
    
    # Clinical Indicators with clinical correlations
    records = []
    
    for i in range(num_records):
        age = ages[i]
        gender = genders[i]
        smoking = smoking_habits[i]
        alcohol = alcohol_habits[i]
        exercise = exercise_levels[i]
        diet = diet_qualities[i]
        
        # Base BMI influenced by exercise and diet
        bmi_base = 26.5
        if exercise == "Sedentary":
            bmi_base += 3.2
        elif exercise == "Light":
            bmi_base += 1.0
        elif exercise == "Vigorous":
            bmi_base -= 2.8
            
        if diet == "Poor":
            bmi_base += 2.5
        elif diet == "Healthy":
            bmi_base -= 2.0
            
        bmi = float(np.clip(np.random.normal(loc=bmi_base, scale=4.8), 17.0, 48.0))
        bmi = round(bmi, 1)
        
        # Blood Pressure: SBP & DBP correlated with age, BMI, smoking, alcohol
        sbp_base = 110 + (age * 0.35) + ((bmi - 24) * 0.9)
        if smoking in ["Current Daily", "Current Occasional"]:
            sbp_base += 6.5
        if alcohol == "Heavy":
            sbp_base += 8.0
        elif alcohol == "Moderate":
            sbp_base += 2.5
            
        sbp = int(np.clip(np.random.normal(loc=sbp_base, scale=12.0), 95, 205))
        
        # DBP loosely correlated with SBP
        dbp_base = 68 + (sbp - 110) * 0.35 + (bmi * 0.2)
        dbp = int(np.clip(np.random.normal(loc=dbp_base, scale=8.0), 55, 125))
        
        # Fasting Blood Glucose (mg/dL) - heavily affected by BMI, age, diet
        glucose_base = 88 + ((bmi - 22) * 1.5) + (age * 0.25)
        if diet == "Poor":
            glucose_base += 15
        elif diet == "Healthy":
            glucose_base -= 6
        if exercise == "Sedentary":
            glucose_base += 8
            
        fasting_glucose = int(np.clip(np.random.normal(loc=glucose_base, scale=24.0), 65, 310))
        
        # Total Cholesterol (mg/dL) - affected by age, diet, smoking
        chol_base = 180 + (age * 0.45) + ((bmi - 23) * 0.8)
        if diet == "Poor":
            chol_base += 22
        elif diet == "Healthy":
            chol_base -= 14
        if smoking == "Current Daily":
            chol_base += 12
            
        total_cholesterol = int(np.clip(np.random.normal(loc=chol_base, scale=28.0), 120, 360))
        
        # Symptom frequencies based on clinical indicators
        # Fatigue
        fatigue_risk = 0.15 + (0.20 if fasting_glucose > 130 else 0) + (0.15 if sbp > 140 else 0) + (0.15 if exercise == "Sedentary" else 0)
        fatigue_val = random.random()
        if fatigue_val < (fatigue_risk * 0.3):
            fatigue = "Chronic/Severe"
        elif fatigue_val < (fatigue_risk * 0.7):
            fatigue = "Frequent"
        elif fatigue_val < fatigue_risk:
            fatigue = "Mild"
        else:
            fatigue = "None"
            
        # Chest Pain
        cp_risk = 0.08 + (0.25 if sbp > 150 else 0) + (0.20 if total_cholesterol > 240 else 0) + (0.18 if smoking == "Current Daily" else 0)
        cp_val = random.random()
        if cp_val < (cp_risk * 0.25):
            chest_pain = "Typical Angina / Severe"
        elif cp_val < (cp_risk * 0.65):
            chest_pain = "Exertional / Discomfort"
        elif cp_val < cp_risk:
            chest_pain = "Atypical"
        else:
            chest_pain = "None"
            
        # Dizziness
        dizz_risk = 0.10 + (0.22 if sbp > 160 or sbp < 100 else 0) + (0.15 if fasting_glucose > 180 or fasting_glucose < 75 else 0)
        dizz_val = random.random()
        if dizz_val < (dizz_risk * 0.3):
            dizziness = "Frequent/Persistent"
        elif dizz_val < (dizz_risk * 0.7):
            dizziness = "Positional"
        elif dizz_val < dizz_risk:
            dizziness = "Occasional"
        else:
            dizziness = "None"
            
        # Chronic Diseases Probability Models
        # 1. Diabetes Probability
        p_diabetes = 0.04
        if fasting_glucose >= 126:
            p_diabetes += 0.68
        elif fasting_glucose >= 100:
            p_diabetes += 0.22
        if bmi >= 30:
            p_diabetes += 0.20
        elif bmi >= 25:
            p_diabetes += 0.08
        if age >= 55:
            p_diabetes += 0.12
        if exercise == "Sedentary":
            p_diabetes += 0.06
        has_diabetes = 1 if (random.random() < min(0.95, p_diabetes)) else 0
        
        # 2. Heart Disease Probability (Coronary Artery Disease / CAD)
        p_heart = 0.03 + (age * 0.004)
        if sbp >= 140 or dbp >= 90:
            p_heart += 0.22
        if total_cholesterol >= 240:
            p_heart += 0.20
        elif total_cholesterol >= 200:
            p_heart += 0.08
        if smoking in ["Current Daily", "Current Occasional"]:
            p_heart += 0.18
        if has_diabetes:
            p_heart += 0.16
        if chest_pain in ["Typical Angina / Severe", "Exertional / Discomfort"]:
            p_heart += 0.25
        has_heart_disease = 1 if (random.random() < min(0.92, p_heart)) else 0
        
        # 3. Stroke Probability
        p_stroke = 0.02 + (age * 0.003)
        if sbp >= 160:
            p_stroke += 0.32
        elif sbp >= 140:
            p_stroke += 0.15
        if smoking == "Current Daily":
            p_stroke += 0.14
        if alcohol == "Heavy":
            p_stroke += 0.12
        if has_heart_disease:
            p_stroke += 0.15
        if has_diabetes:
            p_stroke += 0.10
        if dizziness == "Frequent/Persistent":
            p_stroke += 0.08
        has_stroke = 1 if (random.random() < min(0.88, p_stroke)) else 0
        
        # 4. Chronic Kidney Disease (CKD)
        p_ckd = 0.02 + (0.18 if has_diabetes else 0) + (0.16 if sbp >= 150 else 0) + (0.08 if age >= 65 else 0)
        has_ckd = 1 if (random.random() < min(0.85, p_ckd)) else 0
        
        multimorbidity = has_heart_disease + has_diabetes + has_stroke + has_ckd
        
        # Clinical Risk Score (0 - 100)
        score = 0.0
        score += (age / 88.0) * 18.0
        score += (min(sbp, 200) / 200.0) * 20.0
        score += (min(total_cholesterol, 340) / 340.0) * 15.0
        score += (min(fasting_glucose, 300) / 300.0) * 15.0
        score += (min(bmi, 45) / 45.0) * 10.0
        if smoking == "Current Daily": score += 8.0
        elif smoking == "Current Occasional": score += 4.0
        if alcohol == "Heavy": score += 5.0
        if exercise == "Sedentary": score += 5.0
        score += (multimorbidity * 6.0)
        score = round(min(100.0, max(5.0, score)), 1)
        
        # Risk Tier
        if score >= 75.0 or multimorbidity >= 2 or sbp >= 170:
            risk_tier = "Critical / Urgent"
            recommendation = "Immediate clinical consultation, urgent specialist triage, continuous vital telemetry"
        elif score >= 55.0 or has_heart_disease or has_stroke:
            risk_tier = "High Risk"
            recommendation = "Bi-weekly clinical monitoring, pharmacotherapy review, intensive lifestyle intervention"
        elif score >= 35.0 or has_diabetes or sbp >= 135:
            risk_tier = "Moderate Risk"
            recommendation = "Quarterly health screening, dietary counseling, structured exercise prescription"
        else:
            risk_tier = "Low Risk"
            recommendation = "Annual preventative wellness exam, routine health maintenance"
            
        records.append({
            "patient_id": patient_ids[i],
            "age": age,
            "gender": gender,
            "systolic_bp": sbp,
            "diastolic_bp": dbp,
            "total_cholesterol": total_cholesterol,
            "fasting_glucose": fasting_glucose,
            "bmi": bmi,
            "smoking_habit": smoking,
            "alcohol_consumption": alcohol,
            "exercise_level": exercise,
            "diet_quality": diet,
            "fatigue_condition": fatigue,
            "chest_pain_symptoms": chest_pain,
            "dizziness_patterns": dizziness,
            "heart_disease": has_heart_disease,
            "diabetes": has_diabetes,
            "stroke": has_stroke,
            "kidney_disease": has_ckd,
            "multimorbidity_count": multimorbidity,
            "clinical_risk_score": score,
            "risk_tier": risk_tier,
            "clinical_recommendation": recommendation
        })
        
    df = pd.DataFrame(records)
    return df

def save_to_database_and_csv(df, base_dir):
    raw_dir = os.path.join(base_dir, "data", "raw")
    os.makedirs(raw_dir, exist_ok=True)
    
    csv_path = os.path.join(raw_dir, "chronic_disease_raw.csv")
    df.to_csv(csv_path, index=False)
    print(f"[OK] Raw CSV saved successfully: {csv_path} ({len(df)} records)")
    
    # Also save to raw SQLite database simulating clinical database extraction
    db_path = os.path.join(raw_dir, "hospital_emr_database.db")
    conn = sqlite3.connect(db_path)
    df.to_sql("patient_clinical_records", conn, if_exists="replace", index=False)
    conn.close()
    print(f"[OK] Raw SQLite EMR Database saved: {db_path}")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    print(f"Generating patient health records in {project_root}...")
    dataset = generate_patient_data(6000)
    save_to_database_and_csv(dataset, project_root)
    print("Data collection and extraction stage complete.")
