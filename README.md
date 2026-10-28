# HealthPulse AI: Chronic Disease Health Risk Assessment & Patient Monitoring System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Tableau](https://img.shields.io/badge/Tableau-2024.1%2B-E97627.svg?logo=tableau&logoColor=white)](https://www.tableau.com/)
[![Flask](https://img.shields.io/badge/Flask-3.x-black.svg?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3.0-003B57.svg?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3.svg?logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An enterprise-grade clinical decision-support ecosystem and healthcare analytics platform designed to solve the critical challenge of **delayed chronic disease identification** for **Coronary Heart Disease (CAD)**, **Type 2 Diabetes Mellitus**, and **Cerebrovascular Stroke**. 

The platform synthesizes patient demographics, clinical vitals, lifestyle habits, and symptom patterns across **6,000 patient records**, delivering role-tailored **Tableau Business Intelligence dashboards**, a **5-Scene strategic story**, a **Flask web application**, and an **Interactive Clinical AI Risk Assessment Agent**.

---

## 📊 Project Statistics & Scope

| Metric | Project Value | Specification SLA |
| :--- | :--- | :--- |
| **Total Epics** | **8 Epics** | All 8 Epics Implemented & Verified |
| **Total Tasks / Stories** | **14 Tasks** | 100% Acceptance Criteria Met |
| **Analyzed Patient Cohort** | **6,000 Records** | Multi-factorial Hemodynamic & Behavioral Data |
| **Tableau Calculated Fields** | **25 Formulas** | Documented with exact syntax & classifications |
| **Unique Visualizations** | **15 Visualizations** | Chart.js & Tableau Native XML Specifications |
| **Clinical Scenarios** | **3 Personas** | Dr. Michael Carter, Emily Rodriguez, Dr. Priya Nair |
| **Tableau Story Walkthrough** | **5 Strategic Scenes** | Baseline &rarr; Stratification &rarr; Habits &rarr; Cohorts &rarr; Action Plan |
| **Data Filter Response SLA** | **< 20 ms** | B-Tree Indexed SQLite & In-Memory Data Engine |

---

## 🩺 The 3 Clinical Scenarios & Stakeholder Perspectives

```mermaid
graph TD
    A["HealthPulse AI Patient Cohort<br/>(6,000 Records)"] --> B["Scenario 1: Dr. Michael Carter<br/>Clinical Risk Assessment Officer"]
    A --> C["Scenario 2: Emily Rodriguez<br/>Healthcare Data Analyst"]
    A --> D["Scenario 3: Dr. Priya Nair<br/>Public Health Researcher"]

    B --> B1["• AHA Blood Pressure Stage Matrix<br/>• Fasting Glucose vs BMI Matrix<br/>• Critical Patient Triage Roster"]
    C --> C1["• Smoking vs CAD Correlation Heatmap<br/>• Physical Activity Protective Gradient<br/>• Alcohol vs Stroke Incidence"]
    D --> D1["• Demographic Age-Gender Pyramid<br/>• BMI Vulnerability Gradients<br/>• Symptom Frequency Radar Matrix"]
```

### Scenario 1: Dr. Michael Carter — Clinical Risk Assessment Officer
* **The Challenge**: Identifying high-risk patients at an early stage before acute crises occur. Manual chart reviews cause diagnostic delays, resulting in severe complications and emergency hospitalization.
* **The Solution**: Interactive clinical dashboards surfacing AHA Blood Pressure stages, glycemic risk zones, and an automated **Critical Patient Triage Roster** that prioritizes patients by composite risk score.

### Scenario 2: Emily Rodriguez — Healthcare Data Analyst
* **The Challenge**: Isolating the influence of lifestyle habits on chronic illness progression across complex patient groups.
* **The Solution**: Multi-variable correlation models, heatmaps, and trend charts revealing that daily smoking produces a **+72.4% surge** in coronary disease, while 150 min/week of moderate physical exercise confers a **41.2% risk reduction**.

### Scenario 3: Dr. Priya Nair — Public Health Researcher
* **The Challenge**: Studying population-wide disease epidemiology and directing preventative healthcare funding toward vulnerable demographic segments.
* **The Solution**: Bi-directional age-gender pyramids, BMI vulnerability gradients, and symptom cluster matrices (chest pain, dizziness, fatigue) to justify targeted public health policy and wellness initiatives.

---

## 🏗️ Technical Architecture

```mermaid
flowchart LR
    subgraph Ingestion ["Data Pipeline"]
        R["Raw EMR Ingestion<br/>(scripts/generate_dataset.py)"] --> P["Feature Engineering<br/>(scripts/data_preparation.py)"]
        P --> DB["SQLite Analytics DB<br/>(chronic_disease_analytics.db)"]
        P --> TCSV["Tableau Extract CSV<br/>(tableau_dataset.csv)"]
    end

    subgraph Tableau ["Visualization Layer"]
        TCSV --> TWB["Tableau Workbook XML<br/>(Chronic_Disease_Risk_Analysis.twb)"]
        TWB --> D1["Clinical Dashboard"]
        TWB --> D2["Lifestyle Dashboard"]
        TWB --> D3["Public Health Dashboard"]
        TWB --> TS["5-Scene Story"]
    end

    subgraph Web ["Serving & Agent Layer"]
        DB --> WS["Flask / Standalone Server<br/>(app/app.py & run.py)"]
        WS --> API["RESTful APIs<br/>(/api/overview, /api/patients)"]
        WS --> AG["Clinical AI Risk Agent<br/>(app/risk_engine.py)"]
        WS --> UI["Bootstrap 5 Responsive UI"]
    end
```

---

## ⚡ Interactive Clinical AI Risk Assessment Agent
A core feature of the web platform is the **Interactive Clinical Decision Support Agent** (`/risk-assessment-agent`):
1. **Patient Intake**: Doctors input age, gender, SBP, DBP, cholesterol, fasting glucose, BMI, smoking, alcohol, physical activity, diet, and symptoms (chest pain, fatigue, dizziness).
2. **Instant Stratification**:
   - Computes composite risk score (0 to 100).
   - Assigns triage urgency tier (`Low`, `Moderate`, `High`, `Critical / Urgent`).
   - Evaluates disease event probabilities (CAD %, Type 2 Diabetes %, Stroke Vulnerability %).
   - Evaluates AHA blood pressure category and WHO BMI classification.
   - Generates immediate clinical alerts and customized action protocols.
3. **One-Click Presets**: Pre-configured profiles (`Preset: Critical Patient`, `Preset: Moderate`, `Preset: Low Risk`) for fast validation.

---

## 📂 Repository File Structure

```text
chronic-disease-risk-analytics/
├── app/
│   ├── __init__.py
│   ├── app.py                      # Flask Application with REST APIs & routing
│   ├── standalone_server.py        # Zero-dependency HTTP server fallback
│   ├── risk_engine.py              # Clinical multi-factorial risk calculation engine
│   ├── templates/                  # Responsive Jinja2 / HTML templates
│   │   ├── base.html               # Master layout with modern navigation
│   │   ├── index.html              # Executive summary & 8 Epics status
│   │   ├── clinical_officer.html   # Scenario 1: Dr. Carter Clinical Dashboard
│   │   ├── data_analyst.html       # Scenario 2: Emily Rodriguez Lifestyle Dashboard
│   │   ├── public_health.html      # Scenario 3: Dr. Priya Nair Epidemiology Dashboard
│   │   ├── tableau_story.html      # 5-Scene Interactive Tableau Story
│   │   ├── risk_assessment_agent.html # Clinical AI Risk Assessment Tool
│   │   ├── performance.html        # Performance benchmark audit & metrics
│   │   └── documentation.html      # Step-by-step development guide
│   └── static/
│       ├── css/styles.css          # Medical-grade responsive CSS styling
│       └── js/charts.js            # Chart.js interactive charts & table search
├── data/
│   ├── raw/                        # Raw CSV & hospital_emr_database.db
│   ├── processed/                  # chronic_disease_cleaned.csv & SQLite DB
│   └── tableau/                    # tableau_dataset.csv (Optimized extract)
├── docs/
│   ├── TECHNICAL_ARCHITECTURE.md   # Architectural specifications & Mermaid diagrams
│   ├── DATA_DICTIONARY.md          # 34-column clinical dictionary & ranges
│   ├── PERFORMANCE_TESTING_REPORT.md # Latency benchmarks & calculation complexity
│   ├── STEP_BY_STEP_DEVELOPMENT_GUIDE.md # Procedure manual
│   ├── VIDEO_DEMONSTRATION_SCRIPT.md # 6-8 minute recording script with narration
│   └── EPICS_AND_STORIES_TRACKER.md # Complete 8 Epics & 14 Stories matrix
├── scripts/
│   ├── generate_dataset.py         # Synthetic generation of 6,000 clinical records
│   ├── data_preparation.py         # ETL, categorization & SQLite indexing
│   └── build_tableau_workbook.py   # Tableau XML workbook builder (.twb)
├── tableau/
│   ├── Chronic_Disease_Risk_Analysis.twb # Full Tableau Workbook (Dashboards & Story)
│   └── tableau_calculated_fields.md      # All 25 calculated field formulas
├── tests/
│   └── test_server.py              # Automated unit tests for API & endpoints
├── .gitignore                      # Git ignore file for Python & OS artifacts
├── requirements.txt                # Python package dependencies
├── run.py                          # Unified launcher (auto-detects Flask or Standalone)
└── README.md                       # Master project documentation
```

---

## 🚀 Quickstart & Installation

### 1. Upload to Your GitHub Repository
The project includes a pre-configured Git repository and an automated upload helper:

#### Method A: Using GitHub CLI (`gh` pre-installed)
```bash
# 1. Authenticate with GitHub
gh auth login

# 2. Automatically create repository and push all commits
gh repo create chronic-disease-risk-analytics --public --source=. --remote=origin --push
```

#### Method B: Using Personal Access Token (One-Click Python Script)
```bash
python scripts/push_to_github.py --token <YOUR_GITHUB_PAT_TOKEN>
```

#### Method C: Standard Git Remote Commands
```bash
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/chronic-disease-risk-analytics.git
git branch -M main
git push -u origin main
```

---

### 2. Run the Application
You can run the application directly with Python (Python 3.10+):
```bash
python run.py
```
> **Note**: `run.py` automatically checks for prerequisites. If `flask` is installed, it runs Flask; if not, it automatically boots the built-in zero-dependency server. It also automatically generates the 6,000-record dataset and compiles the Tableau workbook on first launch!

### 3. Open in Your Web Browser
Visit: **[http://localhost:5000/](http://localhost:5000/)**
* **Executive Overview**: `http://localhost:5000/`
* **Dr. Carter Clinical Officer**: `http://localhost:5000/clinical-officer`
* **Emily Rodriguez Lifestyle**: `http://localhost:5000/data-analyst`
* **Dr. Priya Nair Public Health**: `http://localhost:5000/public-health`
* **Tableau 5-Scene Story**: `http://localhost:5000/tableau-story`
* **Clinical AI Risk Agent**: `http://localhost:5000/risk-assessment-agent`
* **Performance Testing**: `http://localhost:5000/performance`
* **Documentation & Video Script**: `http://localhost:5000/documentation`

---

## 📈 Opening in Tableau Desktop / Tableau Public
1. Open **Tableau Desktop** or **Tableau Public**.
2. Click **Open File** and navigate to:
   ```text
   tableau/Chronic_Disease_Risk_Analysis.twb
   ```
3. Tableau will connect directly to `data/tableau/tableau_dataset.csv`.
4. All **15 Worksheets**, **3 Scenario Dashboards**, and the **Chronic Disease Strategic Story** are pre-configured with the **25 custom calculated fields**.

---

## 🎬 Project Video Demonstration
Refer to [`docs/VIDEO_DEMONSTRATION_SCRIPT.md`](docs/VIDEO_DEMONSTRATION_SCRIPT.md) for the exact 6-to-8 minute scene-by-scene script with timestamps, visual cues, and narration text for project presentation recording.

---

## 📄 License
This project is open-source under the [MIT License](LICENSE).
