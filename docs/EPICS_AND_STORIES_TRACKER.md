# Project Epics & User Stories Tracker

This document tracks all **8 Epics** and **14 Stories** defined in the project specification, detailing acceptance criteria and delivered artifacts.

---

| Epic ID | Epic Title | Task / Story ID | User Story & Scope | Delivered Artifact | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **EPIC-01** | **Data Collection & Extraction** | **TASK-01** | Extract patient health records from clinical database with demographic, clinical, and lifestyle variables | `scripts/generate_dataset.py`, `data/raw/chronic_disease_raw.csv` | **Completed** |
| **EPIC-01** | **Data Collection & Extraction** | **TASK-02** | Configure database connection and verify extraction integrity for 6,000 records | `data/raw/hospital_emr_database.db` | **Completed** |
| **EPIC-02** | **Data Preparation** | **TASK-03** | Clean and standardize continuous biomarkers into AHA BP, ADA glucose, and WHO BMI tiers | `scripts/data_preparation.py`, `chronic_disease_cleaned.csv` | **Completed** |
| **EPIC-02** | **Data Preparation** | **TASK-04** | Feature engineer multi-morbidity counts, lifestyle risk indexes, and clinical alert flags | `data/processed/chronic_disease_analytics.db` | **Completed** |
| **EPIC-03** | **Data Visualizations** | **TASK-05** | Design 15 unique visualizations covering hemodynamic, metabolic, behavioral, and demographic dimensions | `app/static/js/charts.js`, Tableau Sheets (1-15) | **Completed** |
| **EPIC-04** | **Scenario Dashboards** | **TASK-06** | Develop Dr. Michael Carter Clinical Risk Assessment & Patient Triage Dashboard (Scenario 1) | `app/templates/clinical_officer.html`, Sheet `Dashboard_Clinical_Risk_Officer` | **Completed** |
| **EPIC-04** | **Scenario Dashboards** | **TASK-07** | Develop Emily Rodriguez Healthcare Data Analyst Lifestyle Correlation Dashboard (Scenario 2) | `app/templates/data_analyst.html`, Sheet `Dashboard_Lifestyle_Data_Analyst` | **Completed** |
| **EPIC-04** | **Scenario Dashboards** | **TASK-08** | Develop Dr. Priya Nair Public Health Researcher Demographic Epidemiology Dashboard (Scenario 3) | `app/templates/public_health.html`, Sheet `Dashboard_Public_Health_Researcher` | **Completed** |
| **EPIC-05** | **Story Development** | **TASK-09** | Build a 5-Scene Tableau Story guiding stakeholders from problem baseline to proactive intervention | `tableau/Chronic_Disease_Risk_Analysis.twb`, `app/templates/tableau_story.html` | **Completed** |
| **EPIC-06** | **Performance Testing** | **TASK-10** | Execute load tests on 6,000 rows, benchmark data filter latencies, and catalog 25 calculated fields | `docs/PERFORMANCE_TESTING_REPORT.md`, `app/templates/performance.html` | **Completed** |
| **EPIC-07** | **Web Integration** | **TASK-11** | Build Flask web application embedding Tableau dashboards, Story, and responsive navigation UI | `app/app.py`, `app/standalone_server.py`, `run.py` | **Completed** |
| **EPIC-07** | **Web Integration** | **TASK-12** | Deploy Interactive Clinical AI Risk Assessment Agent for real-time patient triage scoring | `app/risk_engine.py`, `app/templates/risk_assessment_agent.html` | **Completed** |
| **EPIC-08** | **Demonstration & Docs**| **TASK-13** | Compile end-to-end technical documentation and step-by-step implementation guide | `docs/STEP_BY_STEP_DEVELOPMENT_GUIDE.md`, `docs/TECHNICAL_ARCHITECTURE.md` | **Completed** |
| **EPIC-08** | **Demonstration & Docs**| **TASK-14** | Create scene-by-scene video presentation script for demonstration recording | `docs/VIDEO_DEMONSTRATION_SCRIPT.md` | **Completed** |
