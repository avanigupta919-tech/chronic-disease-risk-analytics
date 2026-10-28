# Technical Architecture Specification

## 1. System Overview
The **Chronic Disease Health Risk Assessment and Patient Monitoring System** is an enterprise-grade medical analytics and clinical decision-support platform designed to address early detection challenges for chronic illnesses including **Coronary Heart Disease**, **Type 2 Diabetes Mellitus**, and **Cerebrovascular Stroke**.

The architecture combines a high-performance **Python/SQLite Data Engineering Pipeline**, a rich **Tableau Visualization Engine** (supporting 3 specialized scenario dashboards and a 5-scene clinical story), and an integrated **Flask Web Application** featuring an **Interactive Clinical Risk Assessment Agent**.

---

## 2. Technical Architecture Diagram

```mermaid
flowchart TD
    subgraph Data_Layer ["1. Data Layer & Ingestion"]
        A1["Hospital EMR Database<br/>(hospital_emr_database.db)"] --> B1["Data Extraction & Collection<br/>(scripts/generate_dataset.py)"]
        B1 --> C1["Raw Patient Dataset<br/>(chronic_disease_raw.csv: 6,000 Records)"]
        C1 --> D1["ETL & Feature Engineering Pipeline<br/>(scripts/data_preparation.py)"]
        D1 --> E1["Indexed SQLite Analytics DB<br/>(chronic_disease_analytics.db)"]
        D1 --> E2["Tableau Optimized Extract<br/>(tableau_dataset.csv)"]
    end

    subgraph Tableau_Engine ["2. Tableau Analytics & Visualization Engine"]
        E2 --> T1["Data Connection & Live Extract"]
        T1 --> T2["25 Custom Calculated Fields<br/>& Dynamic Parameters"]
        T2 --> D_S1["Scenario 1: Clinical Triage Dashboard<br/>(Dr. Michael Carter)"]
        T2 --> D_S2["Scenario 2: Lifestyle Correlation Dashboard<br/>(Emily Rodriguez)"]
        T2 --> D_S3["Scenario 3: Population Health Dashboard<br/>(Dr. Priya Nair)"]
        D_S1 & D_S2 & D_S3 --> T_Story["5-Scene Tableau Story<br/>(Chronic Disease Strategic Storyboard)"]
    end

    subgraph Web_Integration ["3. Flask Web Application & Serving Layer"]
        E1 --> F1["Flask Web Application Core<br/>(app/app.py)"]
        F1 --> F2["RESTful API Endpoints<br/>(/api/overview, /api/patients, /api/assess-risk)"]
        F1 --> F3["Tableau JS API Embedding Connector<br/>(Tableau Public / Server Live Embeds)"]
        F1 --> F4["Clinical Risk Prediction Engine<br/>(AHA/Framingham Risk Scoring Agent)"]
    end

    subgraph Presentation_Layer ["4. User Interface & Stakeholder Dashboards"]
        F1 --> UI1["Executive Overview & Project Stats"]
        F2 & F3 --> UI2["Dr. Carter Clinical Officer View"]
        F2 & F3 --> UI3["Emily Rodriguez Analyst View"]
        F2 & F3 --> UI4["Dr. Priya Nair Public Health View"]
        T_Story --> UI5["Tableau Story Walkthrough"]
        F4 --> UI6["Interactive Patient Risk Assessment Agent"]
        F1 --> UI7["Performance Benchmarks & Docs"]
    end
```

---

## 3. Component Architecture

### A. Data Layer
- **Storage**: SQLite 3 with B-Tree indexes on `risk_tier`, `age_group`, and combined disease diagnosis flags (`heart_disease`, `diabetes`, `stroke`).
- **Feature Engineering**:
  - Continuous-to-categorical binning (AHA Blood Pressure Stages, ADA Glycemic Tiers, WHO BMI Categories, NCEP ATP III Cholesterol Tiers).
  - Multi-factorial risk scoring incorporating hemodynamic, metabolic, lifestyle, and symptomatic markers.
  - Multi-morbidity count (co-occurrence of 0 to 4 chronic diseases).

### B. Tableau Visualization Engine
- **Workbook Structure**: `tableau/Chronic_Disease_Risk_Analysis.twb`
- **Dashboards**:
  1. *Clinical Risk Assessment & Triage* (Dr. Michael Carter): Early warning radar, urgent triage roster, blood pressure vs glucose risk matrix.
  2. *Lifestyle & Behavioral Correlation* (Emily Rodriguez): Smoking & alcohol heatmaps, physical activity protective gradients, diet vs metabolic syndrome.
  3. *Population Demographic Epidemiology* (Dr. Priya Nair): Demographic age-gender pyramids, BMI vulnerability distribution, symptom frequency matrices.
- **Story**: 5-Scene narrative guiding clinical leadership from population illness burden through actionable prevention.

### C. Web Application & AI Agent Layer
- **Framework**: Python Flask 3.x WSGI application.
- **Risk Assessment Agent**: Accepts live patient vitals via modal/form, executes multi-factorial clinical assessment algorithms, generates triage classification, calculates cardiovascular & stroke event risk, and delivers personalized clinical guidelines.
- **Hybrid Embed System**:
  - Live Tableau JavaScript API Embed (`tableau-viz` container) for Tableau Server / Tableau Public integration.
  - Native Chart.js interactive fallback dashboards ensuring full zero-dependency standalone execution.

---

## 4. System Requirements

### Hardware Requirements
- **Processor**: Intel Core i5 / AMD Ryzen 5 or higher (minimum 2.0 GHz)
- **RAM**: Minimum 8 GB (16 GB recommended for high-volume Tableau extracts)
- **Disk Storage**: 500 MB free disk space for dataset, database, and web application assets

### Software Requirements
- **Operating System**: Windows 10/11, macOS 12+, or Ubuntu 20.04+ LTS
- **Tableau**: Tableau Desktop 2022.1+ or Tableau Public (latest version)
- **Python**: Python 3.10, 3.11, or 3.12
- **Web Browser**: Google Chrome, Mozilla Firefox, Microsoft Edge, or Safari (modern evergreen browsers supporting ES6 and WebGL/Canvas)
