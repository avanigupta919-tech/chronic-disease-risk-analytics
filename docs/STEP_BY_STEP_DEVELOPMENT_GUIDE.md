# Step-by-Step Project Development Procedure Guide

This comprehensive guide walks through the complete end-to-end development lifecycle of the **Chronic Disease Health Risk Assessment and Patient Monitoring System**, matching all requirements, Epics, and Story guidelines.

---

## Phase 1: Data Collection & Extraction from Database (Epic 1)
1. **Clinical Modeling**:
   - Model chronic disease dynamics based on empirical clinical criteria:
     - Framingham / ACC / AHA Cardiovascular Risk equations
     - ADA (American Diabetes Association) diagnostic fasting plasma thresholds
     - WHO (World Health Organization) Body Mass Index classifications
2. **Database Ingestion Script (`scripts/generate_dataset.py`)**:
   - Synthesizes 6,000 discrete patient records with realistic correlations:
     - Age, Gender, SBP, DBP, Total Cholesterol, Fasting Glucose, BMI
     - Smoking Habits, Alcohol Consumption, Exercise Levels, Diet Quality
     - Fatigue, Chest Pain, Dizziness symptoms
     - Confirmed diagnoses for Heart Disease, Diabetes, Stroke, Kidney Disease
   - Exports raw data to `data/raw/chronic_disease_raw.csv` and an indexed SQLite database `data/raw/hospital_emr_database.db`.
3. **Execution**:
   ```bash
   python scripts/generate_dataset.py
   ```

---

## Phase 2: Data Preparation & Feature Engineering (Epic 2)
1. **Continuous-to-Categorical Bins (`scripts/data_preparation.py`)**:
   - **Age Groups**: `18-34 Young Adult`, `35-49 Middle Age`, `50-64 Older Adult`, `65+ Senior`
   - **BMI Categories**: `Underweight (<18.5)`, `Normal Weight (18.5-24.9)`, `Overweight (25-29.9)`, `Obese Class I (30-34.9)`, `Obese Class II/III (>=35.0)`
   - **Blood Pressure Stages (AHA)**: `Normal`, `Elevated`, `Hypertension Stage 1`, `Hypertension Stage 2`, `Hypertensive Crisis`
   - **Glucose Bins (ADA)**: `Normal (<100)`, `Prediabetic (100-125)`, `Diabetic (>=126)`
   - **Cholesterol Tiers**: `Desirable (<200)`, `Borderline High (200-239)`, `High (>=240)`
2. **Composite Risk Indicators**:
   - `lifestyle_risk_tier`: Multi-habit index combining smoking, alcohol, exercise, and diet
   - `symptom_severity_tier`: Weighted score for chest pain, dizziness, and fatigue
   - `metabolic_syndrome_flag`: Flagged when BMI >= 30, Glucose >= 100, and SBP >= 130
   - `cardiovascular_warning`: Flagged when SBP >= 140, Cholesterol >= 240, or Angina present
3. **Database Indexing**:
   - Stores cleaned data in `data/processed/chronic_disease_cleaned.csv` and `data/processed/chronic_disease_analytics.db` with B-Tree indexes on `risk_tier` and `age_group`.
4. **Execution**:
   ```bash
   python scripts/data_preparation.py
   ```

---

## Phase 3: Data Visualizations (Epic 3)
1. **Designing 15 Unique Visualizations**:
   - Executive KPI Scorecards (`calc_total_patients`, `calc_high_risk_count`, `calc_heart_disease_rate`, `calc_diabetes_rate`, `calc_stroke_rate`)
   - Blood Pressure SBP vs DBP Stage Scatter
   - Fasting Glucose vs BMI Matrix
   - Cholesterol Across Age Cohorts
   - Multi-morbidity Burden Radial
   - Smoking vs CAD Heatmap
   - Alcohol vs Stroke Incidence
   - Physical Activity Protective Gradient
   - Diet Quality vs Metabolic Syndrome
   - Demographic Age-Gender Pyramid
   - BMI Vulnerability Gradients
   - Symptom Frequency Matrix
   - High-Risk Patient Triage Roster
   - Clinical Risk Score Histogram
   - Prevention & Intervention Opportunity Grid

---

## Phase 4: Responsive Dashboard Design (Epic 4)
1. **Dashboard 1: Dr. Michael Carter (Clinical Risk Assessment Officer)**:
   - Primary Goal: Detect high-risk patients early and triage immediately.
   - Core Features: Triage Alert KPI, BP Distribution, Glucose vs BMI Matrix, Patient Triage Roster.
2. **Dashboard 2: Emily Rodriguez (Healthcare Data Analyst)**:
   - Primary Goal: Identify modifiable lifestyle habits driving chronic illnesses.
   - Core Features: Smoking Heatmaps, Physical Activity Gradient, Alcohol vs Stroke, Diet vs Metabolic Syndrome.
3. **Dashboard 3: Dr. Priya Nair (Public Health Researcher)**:
   - Primary Goal: Study population-wide disease patterns across demographics.
   - Core Features: Demographic Pyramids, BMI Vulnerability Bars, Symptom Radar Matrix, Resource Allocation Grid.

---

## Phase 5: Tableau Story Development (Epic 5)
1. **Authoring 5 Strategic Story Points (`scripts/build_tableau_workbook.py`)**:
   - **Scene 1**: *The Escalating Burden of Chronic Illness* (Population baseline & multi-morbidity breakdown).
   - **Scene 2**: *Clinical Risk Stratification & Early Triage* (Dr. Michael Carter's triage priority).
   - **Scene 3**: *Lifestyle & Behavioral Determinants* (Emily Rodriguez's habit correlations).
   - **Scene 4**: *Vulnerable Populations & Demographic Disparities* (Dr. Priya Nair's epidemiology).
   - **Scene 5**: *Strategic Action Plan: Proactive Interventions & Resource Allocation* (Evidence-based roadmap).
2. **Execution**:
   ```bash
   python scripts/build_tableau_workbook.py
   ```

---

## Phase 6: Performance Testing & Benchmarking (Epic 6)
1. Ingested 6,000 records, benchmarked query execution, and validated all 25 calculated fields.
2. Tested single and composite filter response times: all executed under 20 ms.
3. Generated `docs/PERFORMANCE_TESTING_REPORT.md`.

---

## Phase 7: Web Integration with Flask (Epic 7)
1. **Backend Routing (`app/app.py`)**:
   - Integrates Flask framework with REST API endpoints:
     - `GET /` -> Executive Overview
     - `GET /clinical-officer` -> Dr. Carter Dashboard
     - `GET /data-analyst` -> Emily Rodriguez Dashboard
     - `GET /public-health` -> Dr. Priya Nair Dashboard
     - `GET /tableau-story` -> 5-Scene Story Walkthrough
     - `GET /risk-assessment-agent` -> Interactive AI Calculator
     - `GET /api/overview` -> Real-time summary statistics
     - `GET /api/patients` -> High-risk triage roster filter API
     - `POST /api/assess-risk` -> Patient risk evaluation engine
2. **Built-in Standalone Server (`app/standalone_server.py`)**:
   - Zero-dependency HTTP server fallback so the platform runs immediately in any Python environment.
3. **Frontend UI**:
   - Built with Bootstrap 5.3, FontAwesome 6, and Chart.js 4.4.

---

## Phase 8: Project Demonstration & Documentation (Epic 8)
1. Authored `docs/VIDEO_DEMONSTRATION_SCRIPT.md` with scene-by-scene voiceover narration and visual directions.
2. Prepared technical architecture diagrams and repository files.
3. Packaged into a Git repository ready for GitHub hosting.
