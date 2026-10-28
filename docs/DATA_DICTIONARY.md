# Chronic Disease Patient Monitoring & Analytics — Data Dictionary

## 1. Overview
This dataset contains comprehensive clinical, demographic, behavioral, and symptom records for **6,000 patients**, designed to enable predictive modeling, risk assessment, and clinical visualization across three clinical scenarios:
- **Scenario 1**: Dr. Michael Carter (Clinical Risk Assessment Officer)
- **Scenario 2**: Emily Rodriguez (Healthcare Data Analyst)
- **Scenario 3**: Dr. Priya Nair (Public Health Researcher)

---

## 2. Field Specifications

| Column Name | Data Type | Permitted / Observed Range | Description & Clinical Definition | Scenario Relevance |
| :--- | :--- | :--- | :--- | :--- |
| `patient_id` | String | PAT-10001 to PAT-16000 | Unique alphanumeric hospital patient identifier | Scenarios 1, 2, 3 |
| `age` | Integer | 18 – 88 years | Patient chronological age | Scenarios 1, 3 |
| `age_group` | String | 18-34, 35-49, 50-64, 65+ | Standard epidemiological demographic age cohorts | Scenario 3 (Dr. Priya Nair) |
| `gender` | String | Male, Female | Patient biological gender | Scenarios 1, 3 |
| `systolic_bp` | Integer | 95 – 205 mmHg | Systolic blood pressure (arterial pressure during contraction) | Scenario 1 (Dr. Michael Carter) |
| `diastolic_bp` | Integer | 55 – 125 mmHg | Diastolic blood pressure (arterial pressure between heartbeats) | Scenario 1 |
| `bp_category` | String | Normal, Elevated, Stage 1, Stage 2, Crisis | AHA standard clinical blood pressure stage | Scenario 1 |
| `total_cholesterol` | Integer | 120 – 360 mg/dL | Serum total cholesterol level | Scenario 1 |
| `cholesterol_category` | String | Desirable, Borderline, High Risk | NCEP ATP III clinical lipid tier | Scenario 1 |
| `fasting_glucose` | Integer | 65 – 310 mg/dL | Fasting venous plasma blood glucose | Scenario 1 |
| `glucose_category` | String | Normal, Prediabetic, Diabetic | American Diabetes Association (ADA) diagnostic tier | Scenario 1 |
| `bmi` | Float | 17.0 – 48.0 kg/m² | Body Mass Index (weight in kg / height in m²) | Scenarios 1, 2, 3 |
| `bmi_category` | String | Underweight, Normal, Overweight, Obese I, Obese II/III | WHO standard obesity classification | Scenarios 1, 3 |
| `smoking_habit` | String | Never, Former, Occasional, Daily | Patient tobacco consumption frequency | Scenario 2 (Emily Rodriguez) |
| `alcohol_consumption` | String | None, Low, Moderate, Heavy | Weekly ethanol intake volume classification | Scenario 2 |
| `exercise_level` | String | Sedentary, Light, Moderate, Vigorous | Weekly physical activity tier | Scenario 2 |
| `diet_quality` | String | Poor, Average, Healthy | Nutritional density and adherence to heart-healthy diet | Scenario 2 |
| `fatigue_condition` | String | None, Mild, Frequent, Chronic/Severe | Self-reported energy deficit & chronic exhaustion | Scenario 3 |
| `chest_pain_symptoms` | String | None, Atypical, Exertional, Typical Angina | Symptom manifestation indicating potential ischemic distress | Scenarios 1, 3 |
| `dizziness_patterns` | String | None, Occasional, Positional, Persistent | Vertigo or hemodynamic instability indicators | Scenarios 1, 3 |
| `heart_disease` | Binary (0/1) | 0 = No, 1 = Confirmed | Confirmed coronary artery disease (CAD) / myocardial infarction | Scenarios 1, 2, 3 |
| `diabetes` | Binary (0/1) | 0 = No, 1 = Confirmed | Confirmed Type 2 Diabetes Mellitus diagnosis | Scenarios 1, 2, 3 |
| `stroke` | Binary (0/1) | 0 = No, 1 = Confirmed | History of cerebrovascular accident / ischemic stroke | Scenarios 1, 2, 3 |
| `kidney_disease` | Binary (0/1) | 0 = No, 1 = Confirmed | Chronic Kidney Disease (CKD Stage 2-5) diagnosis | Scenarios 1, 3 |
| `multimorbidity_count`| Integer | 0 – 4 conditions | Sum of diagnosed chronic conditions per patient | Scenarios 1, 3 |
| `clinical_risk_score` | Float | 5.0 – 100.0 | Weighted multi-factorial Framingham/AHA clinical risk score | Scenario 1 (Dr. Carter Triage) |
| `risk_tier` | String | Low, Moderate, High, Critical/Urgent | Triage urgency tier for healthcare resource allocation | Scenarios 1, 3 |
| `cardiovascular_warning`| Binary (0/1) | 0 = No, 1 = Alert | Acute or chronic cardiovascular warning flag | Scenario 1 |
| `metabolic_syndrome_flag`| Binary (0/1) | 0 = No, 1 = Positive | Triple presence: elevated BMI, elevated glucose, elevated BP | Scenario 2 |
| `stroke_vulnerability_index`| Integer | 0 – 15 | Composite score of hemodynamic and lifestyle risk factors | Scenario 2 |
| `clinical_recommendation` | String | Text | Actionable medical protocol & preventative pathway | Scenario 1 |
