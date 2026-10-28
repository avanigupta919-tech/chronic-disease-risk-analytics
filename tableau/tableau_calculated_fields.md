# Tableau Calculated Fields Reference Guide

This document catalogs all **25 Tableau Calculated Fields** created for the **Chronic Disease Health Risk Assessment and Patient Monitoring System**. Each field includes its exact formula syntax, return data type, purpose, and the specific dashboard or scenario in which it is utilized.

---

### 1. Patient Count
- **Formula**: `COUNT([patient_id])`
- **Type**: Number (Integer) / Measure
- **Usage**: KPI Cards, Global patient volume tracking.

---

### 2. High Risk Patient Count
- **Formula**:
  ```tableau
  ZN(SUM(IF [risk_tier] = "High Risk" OR [risk_tier] = "Critical / Urgent" THEN 1 ELSE 0 END))
  ```
- **Type**: Number (Integer) / Measure
- **Usage**: Dr. Michael Carter Clinical Dashboard (Scenario 1) — Triage Alert KPI.

---

### 3. High Risk Prevalence Rate (%)
- **Formula**:
  ```tableau
  [High Risk Patient Count] / [Patient Count] * 100
  ```
- **Type**: Number (Decimal) / Percentage
- **Usage**: Scenario 1 & Scenario 3 — Cohort risk benchmarking.

---

### 4. Heart Disease Prevalence (%)
- **Formula**:
  ```tableau
  SUM([heart_disease]) / [Patient Count] * 100
  ```
- **Type**: Number (Decimal) / Percentage
- **Usage**: Executive KPI, Scenario 1 & 2.

---

### 5. Diabetes Prevalence (%)
- **Formula**:
  ```tableau
  SUM([diabetes]) / [Patient Count] * 100
  ```
- **Type**: Number (Decimal) / Percentage
- **Usage**: Executive KPI, Scenario 1 & 2.

---

### 6. Stroke Prevalence (%)
- **Formula**:
  ```tableau
  SUM([stroke]) / [Patient Count] * 100
  ```
- **Type**: Number (Decimal) / Percentage
- **Usage**: Executive KPI, Scenario 1 & 2.

---

### 7. Multi-morbidity Category
- **Formula**:
  ```tableau
  IF [multimorbidity_count] = 0 THEN "No Chronic Conditions"
  ELSEIF [multimorbidity_count] = 1 THEN "Single Condition"
  ELSEIF [multimorbidity_count] = 2 THEN "Dual Conditions"
  ELSE "Complex Multi-morbidity (3+)"
  END
  ```
- **Type**: String / Dimension
- **Usage**: Multi-morbidity Donut Chart & Patient breakdown.

---

### 8. Blood Pressure Classification (AHA Standard)
- **Formula**:
  ```tableau
  IF [systolic_bp] >= 180 OR [diastolic_bp] >= 120 THEN "Hypertensive Crisis"
  ELSEIF [systolic_bp] >= 140 OR [diastolic_bp] >= 90 THEN "Hypertension Stage 2"
  ELSEIF [systolic_bp] >= 130 OR [diastolic_bp] >= 80 THEN "Hypertension Stage 1"
  ELSEIF [systolic_bp] >= 120 AND [diastolic_bp] < 80 THEN "Elevated"
  ELSE "Normal"
  END
  ```
- **Type**: String / Dimension
- **Usage**: Dr. Carter Clinical Dashboard — BP distribution and color mapping.

---

### 9. Fasting Glucose Diagnostic Tier
- **Formula**:
  ```tableau
  IF [fasting_glucose] < 100 THEN "Normal Glycemia (<100 mg/dL)"
  ELSEIF [fasting_glucose] <= 125 THEN "Impaired / Prediabetes (100-125 mg/dL)"
  ELSE "Diabetic Hyperglycemia (>=126 mg/dL)"
  END
  ```
- **Type**: String / Dimension
- **Usage**: Glucose vs BMI Risk Matrix.

---

### 10. BMI Risk Stratification
- **Formula**:
  ```tableau
  IF [bmi] < 18.5 THEN "Underweight"
  ELSEIF [bmi] < 25.0 THEN "Normal Weight"
  ELSEIF [bmi] < 30.0 THEN "Overweight"
  ELSEIF [bmi] < 35.0 THEN "Class I Obesity"
  ELSE "Class II/III Severe Obesity"
  END
  ```
- **Type**: String / Dimension
- **Usage**: Dr. Priya Nair Demographic Epidemiology Dashboard (Scenario 3).

---

### 11. Cholesterol Risk Tier
- **Formula**:
  ```tableau
  IF [total_cholesterol] < 200 THEN "Desirable (<200 mg/dL)"
  ELSEIF [total_cholesterol] <= 239 THEN "Borderline High (200-239 mg/dL)"
  ELSE "High Hypercholesterolemia (>=240 mg/dL)"
  END
  ```
- **Type**: String / Dimension
- **Usage**: Clinical Risk Dashboard.

---

### 12. Cardiovascular Event Alert Flag
- **Formula**:
  ```tableau
  IF [systolic_bp] >= 160 OR [total_cholesterol] >= 260 OR [chest_pain_symptoms] = "Typical Angina / Severe" THEN "URGENT CARDIAC ALERT"
  ELSEIF [systolic_bp] >= 140 OR [total_cholesterol] >= 240 THEN "ELEVATED RISK"
  ELSE "STABLE"
  END
  ```
- **Type**: String / Dimension
- **Usage**: Triage Table & Alert notifications in Scenario 1.

---

### 13. Metabolic Syndrome Indicator
- **Formula**:
  ```tableau
  IF [bmi] >= 30.0 AND [fasting_glucose] >= 100 AND [systolic_bp] >= 130 THEN 1
  ELSE 0
  END
  ```
- **Type**: Number (Integer) / Measure
- **Usage**: Metabolic Syndrome prevalence tracking across lifestyles.

---

### 14. Metabolic Syndrome Prevalence (%)
- **Formula**:
  ```tableau
  SUM([Metabolic Syndrome Indicator]) / [Patient Count] * 100
  ```
- **Type**: Number (Decimal) / Percentage
- **Usage**: Emily Rodriguez Lifestyle Dashboard (Scenario 2).

---

### 15. Lifestyle Habit Risk Score
- **Formula**:
  ```tableau
  (CASE [smoking_habit]
    WHEN "Current Daily" THEN 3
    WHEN "Current Occasional" THEN 2
    WHEN "Former" THEN 1
    ELSE 0
  END)
  +
  (CASE [alcohol_consumption]
    WHEN "Heavy" THEN 3
    WHEN "Moderate" THEN 1
    ELSE 0
  END)
  +
  (CASE [exercise_level]
    WHEN "Sedentary" THEN 3
    WHEN "Light" THEN 2
    WHEN "Moderate" THEN 1
    ELSE 0
  END)
  +
  (CASE [diet_quality]
    WHEN "Poor" THEN 3
    WHEN "Average" THEN 1
    ELSE 0
  END)
  ```
- **Type**: Number (Integer) / Measure
- **Usage**: Lifestyle Risk Index calculation and correlation analysis.

---

### 16. Lifestyle Risk Classification
- **Formula**:
  ```tableau
  IF [Lifestyle Habit Risk Score] >= 8 THEN "High Behavioral Risk"
  ELSEIF [Lifestyle Habit Risk Score] >= 4 THEN "Moderate Behavioral Risk"
  ELSE "Low Behavioral Risk"
  END
  ```
- **Type**: String / Dimension
- **Usage**: Heatmaps and comparative bar charts in Scenario 2.

---

### 17. Symptom Complexity Score
- **Formula**:
  ```tableau
  (IF [chest_pain_symptoms] = "Typical Angina / Severe" THEN 3
   ELSEIF [chest_pain_symptoms] = "Exertional / Discomfort" THEN 2
   ELSEIF [chest_pain_symptoms] = "Atypical" THEN 1
   ELSE 0 END)
  +
  (IF [fatigue_condition] = "Chronic/Severe" THEN 2
   ELSEIF [fatigue_condition] = "Frequent" THEN 1
   ELSE 0 END)
  +
  (IF [dizziness_patterns] = "Frequent/Persistent" THEN 2
   ELSEIF [dizziness_patterns] IN ("Positional", "Occasional") THEN 1
   ELSE 0 END)
  ```
- **Type**: Number (Integer) / Measure
- **Usage**: Dr. Priya Nair Symptom & Disease Correlation Matrix.

---

### 18. Symptom Urgency Category
- **Formula**:
  ```tableau
  IF [Symptom Complexity Score] >= 5 THEN "High Symptom Burden"
  ELSEIF [Symptom Complexity Score] >= 2 THEN "Moderate Symptom Burden"
  ELSEIF [Symptom Complexity Score] = 1 THEN "Mild Symptom Burden"
  ELSE "Asymptomatic"
  END
  ```
- **Type**: String / Dimension
- **Usage**: Symptom Trellis & Stacked Bars.

---

### 19. Stroke Vulnerability Score
- **Formula**:
  ```tableau
  (IF [systolic_bp] >= 160 THEN 3 ELSEIF [systolic_bp] >= 140 THEN 1 ELSE 0 END)
  + (IF [smoking_habit] = "Current Daily" THEN 2 ELSE 0 END)
  + (IF [alcohol_consumption] = "Heavy" THEN 2 ELSE 0 END)
  + (IF [age] >= 65 THEN 2 ELSE 0 END)
  + (IF [heart_disease] = 1 THEN 2 ELSE 0 END)
  + (IF [dizziness_patterns] = "Frequent/Persistent" THEN 1 ELSE 0 END)
  ```
- **Type**: Number (Integer) / Measure
- **Usage**: Stroke Risk Stratification Visualizations.

---

### 20. Age Cohort Bins
- **Formula**:
  ```tableau
  IF [age] < 35 THEN "18-34 Young Adult"
  ELSEIF [age] < 50 THEN "35-49 Middle Age"
  ELSEIF [age] < 65 THEN "50-64 Older Adult"
  ELSE "65+ Senior"
  END
  ```
- **Type**: String / Dimension
- **Usage**: Scenario 3 Demographic Pyramids and Age distributions.

---

### 21. Dynamic Metric Selection (Parameter-Driven)
- **Parameter Name**: `p_Select_Metric` (Values: "Risk Score", "Systolic BP", "Total Cholesterol", "Fasting Glucose", "BMI")
- **Formula**:
  ```tableau
  CASE [p_Select_Metric]
    WHEN "Risk Score" THEN [clinical_risk_score]
    WHEN "Systolic BP" THEN [systolic_bp]
    WHEN "Total Cholesterol" THEN [total_cholesterol]
    WHEN "Fasting Glucose" THEN [fasting_glucose]
    WHEN "BMI" THEN [bmi]
  END
  ```
- **Type**: Number (Decimal) / Measure
- **Usage**: Dynamic parameter-controlled comparative charts across dashboards.

---

### 22. Color Code by Risk Tier
- **Formula**:
  ```tableau
  CASE [risk_tier]
    WHEN "Critical / Urgent" THEN "#DC2626"   /* Crimson Red */
    WHEN "High Risk" THEN "#EA580C"           /* Amber Orange */
    WHEN "Moderate Risk" THEN "#F59E0B"       /* Yellow Gold */
    WHEN "Low Risk" THEN "#10B981"            /* Emerald Green */
    ELSE "#6B7280"
  END
  ```
- **Type**: String / Attribute (Hex Color)
- **Usage**: Uniform color harmony across all 15+ visualizations.

---

### 23. Average Clinical Risk Score
- **Formula**: `AVG([clinical_risk_score])`
- **Type**: Number (Decimal) / Measure
- **Usage**: Scenario 1, 2, 3 KPI comparison.

---

### 24. Prevention Opportunity Flag
- **Formula**:
  ```tableau
  IF [risk_tier] = "Moderate Risk" AND [exercise_level] IN ("Sedentary", "Light") AND [smoking_habit] != "Never"
  THEN "High Opportunity for Lifestyle Reversal"
  ELSEIF [risk_tier] = "High Risk" AND [multimorbidity_count] <= 1
  THEN "Clinical Pharmacotherapy Opportunity"
  ELSE "Standard Care"
  END
  ```
- **Type**: String / Dimension
- **Usage**: Public Health & Preventive Care Action Planning (Scene 5).

---

### 25. Clinical Action Recommendation Text
- **Formula**:
  ```tableau
  IF [risk_tier] = "Critical / Urgent" THEN "Immediate inpatient triage, telemetry, cardiology consultation"
  ELSEIF [risk_tier] = "High Risk" THEN "Specialist referral within 7 days, dual-therapy medication review"
  ELSEIF [risk_tier] = "Moderate Risk" THEN "Lifestyle intervention program, 3-month follow-up lab screening"
  ELSE "Annual preventative wellness exam"
  END
  ```
- **Type**: String / Dimension
- **Usage**: Patient Detail Tooltip and Drill-through Roster.
