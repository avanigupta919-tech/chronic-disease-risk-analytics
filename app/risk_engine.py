"""
Clinical Risk Assessment Engine
Implements multi-factorial clinical assessment algorithms based on AHA/Framingham/ACC/ADA guidelines:
- Evaluates Cardiovascular Event Risk (10-year CAD/MI risk)
- Evaluates Type 2 Diabetes Progression Risk
- Evaluates Cerebrovascular Stroke Vulnerability
- Computes Overall Clinical Risk Score (0-100)
- Assigns Triage Urgency Tier (Low, Moderate, High, Critical)
- Generates Tailored Clinical Recommendations & Action Protocols
"""

def evaluate_patient_risk(data):
    """
    Input data dict:
    - age: int
    - gender: str ('Male', 'Female')
    - systolic_bp: int
    - diastolic_bp: int
    - total_cholesterol: int
    - fasting_glucose: int
    - bmi: float
    - smoking_habit: str ('Never', 'Former', 'Current Occasional', 'Current Daily')
    - alcohol_consumption: str ('None', 'Low', 'Moderate', 'Heavy')
    - exercise_level: str ('Sedentary', 'Light', 'Moderate', 'Vigorous')
    - diet_quality: str ('Poor', 'Average', 'Healthy')
    - chest_pain_symptoms: str ('None', 'Atypical', 'Exertional / Discomfort', 'Typical Angina / Severe')
    - fatigue_condition: str ('None', 'Mild', 'Frequent', 'Chronic/Severe')
    - dizziness_patterns: str ('None', 'Occasional', 'Positional', 'Frequent/Persistent')
    """
    age = int(data.get("age", 50))
    gender = data.get("gender", "Male")
    sbp = int(data.get("systolic_bp", 120))
    dbp = int(data.get("diastolic_bp", 80))
    chol = int(data.get("total_cholesterol", 190))
    glucose = int(data.get("fasting_glucose", 95))
    bmi = float(data.get("bmi", 24.5))
    smoking = data.get("smoking_habit", "Never")
    alcohol = data.get("alcohol_consumption", "None")
    exercise = data.get("exercise_level", "Moderate")
    diet = data.get("diet_quality", "Average")
    chest_pain = data.get("chest_pain_symptoms", "None")
    fatigue = data.get("fatigue_condition", "None")
    dizziness = data.get("dizziness_patterns", "None")

    # 1. Cardiovascular Risk Score (0 - 100%)
    cad_score = 5.0 + (age * 0.35)
    if sbp >= 160: cad_score += 25
    elif sbp >= 140: cad_score += 15
    elif sbp >= 130: cad_score += 8
    
    if chol >= 240: cad_score += 20
    elif chol >= 200: cad_score += 10
    
    if smoking == "Current Daily": cad_score += 18
    elif smoking == "Current Occasional": cad_score += 8
    
    if chest_pain == "Typical Angina / Severe": cad_score += 25
    elif chest_pain == "Exertional / Discomfort": cad_score += 15
    elif chest_pain == "Atypical": cad_score += 5
    
    if exercise == "Sedentary": cad_score += 8
    cad_score = min(98.0, round(cad_score, 1))

    # 2. Diabetes Risk Score (0 - 100%)
    diab_score = 4.0
    if glucose >= 126: diab_score += 65
    elif glucose >= 100: diab_score += 28
    
    if bmi >= 35.0: diab_score += 25
    elif bmi >= 30.0: diab_score += 18
    elif bmi >= 25.0: diab_score += 8
    
    if age >= 50: diab_score += 10
    if diet == "Poor": diab_score += 10
    if exercise == "Sedentary": diab_score += 8
    diab_score = min(98.0, round(diab_score, 1))

    # 3. Stroke Vulnerability Score (0 - 100%)
    stroke_score = 3.0 + (age * 0.30)
    if sbp >= 160: stroke_score += 30
    elif sbp >= 140: stroke_score += 16
    
    if smoking == "Current Daily": stroke_score += 15
    if alcohol == "Heavy": stroke_score += 14
    if dizziness == "Frequent/Persistent": stroke_score += 12
    if cad_score > 60: stroke_score += 10
    stroke_score = min(96.0, round(stroke_score, 1))

    # 4. Overall Clinical Risk Score (0 - 100)
    composite = (cad_score * 0.38) + (diab_score * 0.32) + (stroke_score * 0.30)
    composite = min(100.0, max(5.0, round(composite, 1)))

    # 5. Triage Tier & Clinical Recommendation
    alerts = []
    if sbp >= 180 or dbp >= 120:
        alerts.append("CRITICAL: Hypertensive Crisis Threshold Reached (Immediate Medical Intervention Required)")
    elif sbp >= 140 or dbp >= 90:
        alerts.append("ALERT: Hypertension Stage 2 detected")

    if glucose >= 126:
        alerts.append("ALERT: Hyperglycemia in diabetic diagnostic range (>=126 mg/dL)")
    elif glucose >= 100:
        alerts.append("NOTICE: Impaired fasting glucose / pre-diabetic marker")

    if chol >= 240:
        alerts.append("ALERT: Severe hypercholesterolemia (>=240 mg/dL)")

    if chest_pain in ["Typical Angina / Severe", "Exertional / Discomfort"]:
        alerts.append("URGENT: Ischemic cardiac symptoms reported — ECG and troponin testing indicated")

    # Classification
    if composite >= 75.0 or sbp >= 180 or chest_pain == "Typical Angina / Severe":
        tier = "Critical / Urgent"
        badge_color = "danger"
        recommendations = [
            "Immediate Inpatient Emergency Triage and 12-lead Electrocardiogram (ECG)",
            "Urgent Cardiology and Endocrinology Specialist Consultation",
            "Continuous vital sign telemetry (automated BP/HR monitoring)",
            "Stat lipid panel, HbA1c, hs-CRP, and troponin baseline testing",
            "Intensive medication protocol: Antihypertensive dual therapy & Statin initiation"
        ]
    elif composite >= 55.0 or sbp >= 140 or diab_score >= 60:
        tier = "High Risk"
        badge_color = "warning"
        recommendations = [
            "Specialist clinical referral scheduled within 5 to 7 days",
            "Comprehensive 24-hour ambulatory blood pressure monitoring (ABPM)",
            "Structured pharmacotherapy review and titration",
            "Clinical nutrition referral for low-glycemic, Mediterranean dietary protocol",
            "Smoking cessation program enrollment with pharmacological support"
        ]
    elif composite >= 35.0 or bmi >= 30.0 or glucose >= 100:
        tier = "Moderate Risk"
        badge_color = "info"
        recommendations = [
            "Quarterly outpatient preventative wellness checkups",
            "Lifestyle modification program: 150 minutes/week moderate aerobic exercise",
            "Home blood pressure monitoring log (twice weekly)",
            "Dietary counseling to reduce saturated fats and refined sugars",
            "Repeat fasting lipid and glucose panel in 90 days"
        ]
    else:
        tier = "Low Risk"
        badge_color = "success"
        recommendations = [
            "Maintain current healthy active lifestyle and balanced dietary habits",
            "Annual preventative routine physical examination and screening",
            "Ongoing cardiovascular health maintenance and wellness education"
        ]

    # AHA Blood pressure stage
    if sbp >= 180 or dbp >= 120: bp_stage = "Hypertensive Crisis"
    elif sbp >= 140 or dbp >= 90: bp_stage = "Hypertension Stage 2"
    elif sbp >= 130 or dbp >= 80: bp_stage = "Hypertension Stage 1"
    elif sbp >= 120 and dbp < 80: bp_stage = "Elevated"
    else: bp_stage = "Normal"

    # BMI stage
    if bmi < 18.5: bmi_tier = "Underweight (<18.5)"
    elif bmi < 25.0: bmi_tier = "Normal Weight (18.5-24.9)"
    elif bmi < 30.0: bmi_tier = "Overweight (25.0-29.9)"
    elif bmi < 35.0: bmi_tier = "Obese Class I (30.0-34.9)"
    else: bmi_tier = "Obese Class II/III (>=35.0)"

    return {
        "overall_risk_score": composite,
        "risk_tier": tier,
        "badge_color": badge_color,
        "cad_risk_pct": cad_score,
        "diabetes_risk_pct": diab_score,
        "stroke_risk_pct": stroke_score,
        "bp_stage": bp_stage,
        "bmi_tier": bmi_tier,
        "clinical_alerts": alerts,
        "recommendations": recommendations
    }
