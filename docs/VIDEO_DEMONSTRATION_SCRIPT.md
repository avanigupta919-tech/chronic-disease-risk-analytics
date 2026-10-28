# Video Demonstration Script: Chronic Disease Risk Platform

## Project Overview
- **Project Title**: Chronic Disease Health Risk Assessment and Patient Monitoring System
- **Technologies Used**: Python, SQLite, Tableau Desktop, Flask Web Framework, Chart.js, Bootstrap 5
- **Demonstration Target Duration**: 6 to 8 Minutes

---

## Scene-by-Scene Recording Plan

### Segment 1: Title Screen & Executive Overview (0:00 - 1:15)
- **Visual**: Open browser to `http://localhost:5000/`. Highlight the header banner, KPI metric cards, and the 8 Epics status table.
- **Narration**:
  > *"Hello everyone. Today I will present our complete end-to-end solution for the Chronic Disease Health Risk Assessment and Patient Monitoring System.*
  > 
  > *Chronic illnesses—primarily Coronary Heart Disease, Diabetes, and Stroke—represent one of the greatest challenges facing healthcare providers. Delayed diagnosis leads to avoidable medical complications, severe treatment costs, and diminished patient outcomes.*
  > 
  > *Our platform bridges this gap by synthesizing demographic indicators, clinical vitals, and lifestyle habits across 6,000 patients. We have implemented 8 full Epics, 14 Stories, 25 Tableau calculated fields, 15 unique visualizations, and an integrated web platform built on Flask and Tableau."*

---

### Segment 2: Scenario 1 — Dr. Michael Carter (Clinical Risk Officer) (1:15 - 2:45)
- **Visual**: Click on **"Dr. Michael Carter (Clinical)"** in the top navigation bar (`/clinical-officer`). Hover over the Blood Pressure Stage Distribution and Fasting Glucose vs BMI Matrix. Scroll down to the High-Risk Patient Triage Roster and type `10042` in the search bar.
- **Narration**:
  > *"Let's explore our first scenario: Dr. Michael Carter, Clinical Risk Assessment Officer.*
  > 
  > *Dr. Carter faces the challenge of identifying high-risk patients early before acute cardiovascular emergencies strike. In our clinical dashboard, Dr. Carter is immediately alerted that 642 patients require Critical / Urgent triage.*
  > 
  > *Our Blood Pressure Stage Distribution classifies patients according to AHA standards, showing over 1,900 patients in Stage 2 Hypertension. Right next to it, our Fasting Glucose vs. BMI matrix highlights the rapid surge of diabetic hyperglycemia when BMI surpasses 30.*
  > 
  > *Dr. Carter can use the interactive triage roster to drill down into specific patient IDs, verify their clinical markers, and review immediate protocol recommendations—such as emergency telemetry and stat statin initiation."*

---

### Segment 3: Scenario 2 — Emily Rodriguez (Healthcare Data Analyst) (2:45 - 4:00)
- **Visual**: Navigate to **"Emily Rodriguez (Lifestyle)"** (`/data-analyst`). Highlight the Smoking Habit vs CAD chart and the Physical Activity Protective Gradient line chart.
- **Narration**:
  > *"In Scenario 2, we look at the platform through the lens of Emily Rodriguez, our Healthcare Data Analyst.*
  > 
  > *Emily needs to understand how modifiable behaviors influence chronic disease occurrence across patient cohorts. Manually analyzing large medical datasets makes finding these relationships difficult.*
  > 
  > *Our comparative analytics show that Current Daily Smoking surges Heart Disease prevalence to 38.6%—a 72% relative increase over never-smokers. Conversely, our physical activity gradient demonstrates that 150 minutes of weekly moderate exercise reduces overall chronic disease burden by 41.2%.*
  > 
  > *These visual analytics empower healthcare teams to design evidence-based preventative wellness programs."*

---

### Segment 4: Scenario 3 — Dr. Priya Nair (Public Health Researcher) (4:00 - 5:15)
- **Visual**: Click on **"Dr. Priya Nair (Population)"** (`/public-health`). Showcase the Demographic Age-Gender Pyramid and the Symptom Frequency Radar Matrix.
- **Narration**:
  > *"In Scenario 3, Dr. Priya Nair studies population-wide epidemiology and demographic disparities.*
  > 
  > *Our bi-directional demographic pyramid illustrates that chronic morbidity escalates rapidly beyond age 50, reaching 36.8% CAD prevalence in senior citizens. Additionally, our symptom radar matrix highlights that chronic fatigue and exertional chest pain strongly cluster together in high-risk patients.*
  > 
  > *These population-level insights allow public health authorities to target health policy and preventative screening funds where they produce the highest return on investment."*

---

### Segment 5: Tableau Story & Interactive AI Risk Agent (5:15 - 6:45)
- **Visual**: Click on **"Tableau Story"** (`/tableau-story`). Walk through Scenes 1 to 5. Then click on **"Risk Agent"** (`/risk-assessment-agent`). Click the preset button **"Preset: Critical Patient"**, and click **"Compute Multi-Factorial Clinical Assessment"**. Show the real-time score calculation and alerts.
- **Narration**:
  > *"To provide an executive-level walkthrough, we constructed a 5-Scene Tableau Story that synthesizes clinical risk, lifestyle determinants, demographic vulnerabilities, and strategic prevention into an intuitive narrative.*
  > 
  > *Furthermore, we built an interactive Clinical AI Risk Assessment Agent. Clinicians can input live patient vitals—or click preset patient profiles—to receive an instantaneous multi-factorial risk prediction.*
  > 
  > *Here, the agent computes an overall score of 76.8 out of 100, assigns the patient to the Critical / Urgent Triage Tier, maps the AHA blood pressure stage, detects diabetic hyperglycemia, and provides specific medical protocols."*

---

### Segment 6: Performance Testing & GitHub Publishing (6:45 - 7:30)
- **Visual**: Click on **"Performance"** (`/performance`) to show the sub-20ms query latency benchmarks and 25 calculated fields table. Show the project GitHub repository folder structure.
- **Narration**:
  > *"Performance testing confirms that our database indexes and optimized Tableau extracts maintain sub-20 millisecond filter response times across all 6,000 records.*
  > 
  > *The entire codebase, SQLite database, Tableau workbook XML, Flask application, and documentation are committed and published to GitHub.*
  > 
  > *Thank you very much for watching our presentation!"*
