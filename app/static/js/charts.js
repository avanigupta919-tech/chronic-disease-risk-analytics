// HealthPulse AI - Interactive Visualizations Engine (Chart.js)

document.addEventListener("DOMContentLoaded", function () {
  // Scenario 1: Dr. Michael Carter Clinical Dashboard Charts
  initClinicalCharts();

  // Scenario 2: Emily Rodriguez Data Analyst Charts
  initAnalystCharts();

  // Scenario 3: Dr. Priya Nair Public Health Charts
  initPublicHealthCharts();

  // Patient Roster Interactive Search & Filter
  initTriageRosterInteractivity();
});

function initClinicalCharts() {
  // 1. Blood Pressure Stage Distribution
  const bpCanvas = document.getElementById("chart-bp-distribution");
  if (bpCanvas) {
    new Chart(bpCanvas.getContext("2d"), {
      type: "bar",
      data: {
        labels: ["Normal (<120)", "Elevated (120-129)", "Stage 1 (130-139)", "Stage 2 (140-179)", "Crisis (>=180)"],
        datasets: [{
          label: "Number of Patients",
          data: [1340, 980, 1740, 1580, 360],
          backgroundColor: ["#10b981", "#38bdf8", "#f59e0b", "#ea580c", "#dc2626"],
          borderRadius: 6
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              afterLabel: function(ctx) {
                const total = 6000;
                const pct = ((ctx.parsed.y / total) * 100).toFixed(1);
                return `Proportion: ${pct}% of cohort`;
              }
            }
          }
        },
        scales: {
          y: { beginAtZero: true, grid: { color: "#f1f5f9" } },
          x: { grid: { display: false } }
        }
      }
    });
  }

  // 2. Fasting Glucose vs BMI Dual Risk Matrix
  const glucoseCanvas = document.getElementById("chart-glucose-bmi");
  if (glucoseCanvas) {
    new Chart(glucoseCanvas.getContext("2d"), {
      type: "bar",
      data: {
        labels: ["Underweight", "Normal Weight", "Overweight", "Obese Class I", "Obese Class II/III"],
        datasets: [
          {
            label: "Normal Glycemia (<100 mg/dL)",
            data: [120, 1140, 780, 420, 210],
            backgroundColor: "#10b981",
            stack: "Stack 0",
            borderRadius: 4
          },
          {
            label: "Prediabetic (100-125 mg/dL)",
            data: [35, 420, 740, 680, 270],
            backgroundColor: "#f59e0b",
            stack: "Stack 0",
            borderRadius: 4
          },
          {
            label: "Diabetic Hyperglycemia (>=126 mg/dL)",
            data: [15, 120, 310, 440, 300],
            backgroundColor: "#dc2626",
            stack: "Stack 0",
            borderRadius: 4
          }
        ]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { position: "top", labels: { boxWidth: 12 } }
        },
        scales: {
          y: { beginAtZero: true, stacked: true, grid: { color: "#f1f5f9" } },
          x: { stacked: true, grid: { display: false } }
        }
      }
    });
  }
}

function initAnalystCharts() {
  // 1. Smoking Habit vs Heart Disease & Stroke
  const smokingCanvas = document.getElementById("chart-smoking-cad");
  if (smokingCanvas) {
    new Chart(smokingCanvas.getContext("2d"), {
      type: "bar",
      data: {
        labels: ["Never Smoked", "Former Smoker", "Current Occasional", "Current Daily"],
        datasets: [
          {
            label: "Heart Disease Rate (%)",
            data: [14.2, 21.8, 29.4, 38.6],
            backgroundColor: "#dc2626",
            borderRadius: 6
          },
          {
            label: "Stroke Rate (%)",
            data: [4.8, 7.2, 9.8, 14.5],
            backgroundColor: "#ea580c",
            borderRadius: 6
          }
        ]
      },
      options: {
        responsive: true,
        plugins: { legend: { position: "top" } },
        scales: {
          y: { beginAtZero: true, max: 45, ticks: { callback: v => v + "%" }, grid: { color: "#f1f5f9" } },
          x: { grid: { display: false } }
        }
      }
    });
  }

  // 2. Physical Activity Protective Gradient
  const exerciseCanvas = document.getElementById("chart-exercise-gradient");
  if (exerciseCanvas) {
    new Chart(exerciseCanvas.getContext("2d"), {
      type: "line",
      data: {
        labels: ["Sedentary", "Light (1-2x/wk)", "Moderate (3-4x/wk)", "Vigorous (5+x/wk)"],
        datasets: [{
          label: "Overall High-Risk Proportion (%)",
          data: [39.4, 27.6, 17.2, 11.4],
          borderColor: "#16a34a",
          backgroundColor: "rgba(22, 163, 74, 0.12)",
          fill: true,
          tension: 0.35,
          pointRadius: 6,
          pointHoverRadius: 8
        }]
      },
      options: {
        responsive: true,
        scales: {
          y: { beginAtZero: true, max: 50, ticks: { callback: v => v + "%" }, grid: { color: "#f1f5f9" } },
          x: { grid: { display: false } }
        }
      }
    });
  }

  // 3. Alcohol vs Stroke
  const alcoholCanvas = document.getElementById("chart-alcohol-stroke");
  if (alcoholCanvas) {
    new Chart(alcoholCanvas.getContext("2d"), {
      type: "bar",
      data: {
        labels: ["None", "Low (<3/wk)", "Moderate (3-7/wk)", "Heavy (>7/wk)"],
        datasets: [{
          label: "Stroke Incidence (%)",
          data: [4.9, 5.8, 9.4, 16.8],
          backgroundColor: ["#38bdf8", "#0284c7", "#f59e0b", "#dc2626"],
          borderRadius: 6
        }]
      },
      options: {
        responsive: true,
        plugins: { legend: { display: false } },
        scales: {
          y: { beginAtZero: true, max: 20, ticks: { callback: v => v + "%" }, grid: { color: "#f1f5f9" } },
          x: { grid: { display: false } }
        }
      }
    });
  }

  // 4. Diet Quality vs Metabolic Syndrome
  const dietCanvas = document.getElementById("chart-diet-syndrome");
  if (dietCanvas) {
    new Chart(dietCanvas.getContext("2d"), {
      type: "doughnut",
      data: {
        labels: ["Poor Diet (44.8% Syn.)", "Average Diet (23.4% Syn.)", "Healthy Diet (9.8% Syn.)"],
        datasets: [{
          data: [44.8, 23.4, 9.8],
          backgroundColor: ["#dc2626", "#f59e0b", "#10b981"]
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { position: "bottom" },
          tooltip: {
            callbacks: {
              label: ctx => ` ${ctx.label}: ${ctx.raw}% diagnosed with metabolic syndrome`
            }
          }
        }
      }
    });
  }
}

function initPublicHealthCharts() {
  // 1. Demographic Age-Gender Pyramid
  const demoCanvas = document.getElementById("chart-demographic-pyramid");
  if (demoCanvas) {
    new Chart(demoCanvas.getContext("2d"), {
      type: "bar",
      data: {
        labels: ["18-34 Young Adult", "35-49 Middle Age", "50-64 Older Adult", "65+ Senior"],
        datasets: [
          {
            label: "Male High Risk (%)",
            data: [8.5, 18.4, 32.6, 44.2],
            backgroundColor: "#0284c7",
            borderRadius: 6
          },
          {
            label: "Female High Risk (%)",
            data: [6.8, 15.2, 28.9, 41.0],
            backgroundColor: "#ec4899",
            borderRadius: 6
          }
        ]
      },
      options: {
        responsive: true,
        plugins: { legend: { position: "top" } },
        scales: {
          y: { beginAtZero: true, max: 50, ticks: { callback: v => v + "%" }, grid: { color: "#f1f5f9" } },
          x: { grid: { display: false } }
        }
      }
    });
  }

  // 2. BMI Vulnerability Gradients
  const bmiCanvas = document.getElementById("chart-bmi-vulnerability");
  if (bmiCanvas) {
    new Chart(bmiCanvas.getContext("2d"), {
      type: "bar",
      data: {
        labels: ["Underweight", "Normal Weight", "Overweight", "Obese Class I", "Obese Class II/III"],
        datasets: [
          {
            label: "Diabetes Prevalence (%)",
            data: [6.2, 11.4, 21.8, 31.4, 42.8],
            backgroundColor: "#0891b2",
            borderRadius: 6
          },
          {
            label: "Heart Disease (%)",
            data: [12.0, 16.2, 24.5, 30.1, 38.4],
            backgroundColor: "#ea580c",
            borderRadius: 6
          }
        ]
      },
      options: {
        responsive: true,
        plugins: { legend: { position: "top" } },
        scales: {
          y: { beginAtZero: true, max: 50, ticks: { callback: v => v + "%" }, grid: { color: "#f1f5f9" } },
          x: { grid: { display: false } }
        }
      }
    });
  }

  // 3. Symptom Frequency Matrix
  const sympCanvas = document.getElementById("chart-symptom-patterns");
  if (sympCanvas) {
    new Chart(sympCanvas.getContext("2d"), {
      type: "radar",
      data: {
        labels: ["Severe Chest Pain", "Exertional Discomfort", "Chronic Fatigue", "Frequent Dizziness", "Positional Vertigo"],
        datasets: [
          {
            label: "Critical / High Risk Cohort",
            data: [78, 65, 84, 56, 42],
            borderColor: "#dc2626",
            backgroundColor: "rgba(220, 38, 38, 0.2)",
            pointRadius: 4
          },
          {
            label: "Low / Moderate Risk Cohort",
            data: [8, 18, 24, 15, 12],
            borderColor: "#10b981",
            backgroundColor: "rgba(16, 185, 129, 0.2)",
            pointRadius: 4
          }
        ]
      },
      options: {
        responsive: true,
        scales: {
          r: { beginAtZero: true, max: 100 }
        }
      }
    });
  }

  // 4. Policy Resource Allocation
  const policyCanvas = document.getElementById("chart-policy-allocation");
  if (policyCanvas) {
    new Chart(policyCanvas.getContext("2d"), {
      type: "bar",
      data: {
        labels: ["Critical Care & Telemetry", "Specialist Dual-Therapy", "Community Lifestyle Reversal", "Routine Screening"],
        datasets: [{
          label: "Recommended Budget Allocation (%)",
          data: [35, 25, 30, 10],
          backgroundColor: ["#dc2626", "#f59e0b", "#10b981", "#3b82f6"],
          borderRadius: 6
        }]
      },
      options: {
        responsive: true,
        plugins: { legend: { display: false } },
        scales: {
          y: { beginAtZero: true, max: 40, ticks: { callback: v => v + "%" }, grid: { color: "#f1f5f9" } },
          x: { grid: { display: false } }
        }
      }
    });
  }
}

function initTriageRosterInteractivity() {
  const searchInput = document.getElementById("roster-search");
  const tierFilter = document.getElementById("roster-filter-tier");
  const tbody = document.getElementById("triage-tbody");

  if (!tbody || !searchInput || !tierFilter) return;

  function filterRows() {
    const term = searchInput.value.toUpperCase();
    const tier = tierFilter.value;
    const rows = tbody.querySelectorAll("tr");

    rows.forEach(row => {
      const idText = row.cells[0].textContent.toUpperCase();
      const tierText = row.cells[7].textContent.trim();

      const matchesTerm = idText.includes(term);
      const matchesTier = (tier === "ALL") || (tierText.includes(tier));

      if (matchesTerm && matchesTier) {
        row.style.display = "";
      } else {
        row.style.display = "none";
      }
    });
  }

  searchInput.addEventListener("input", filterRows);
  tierFilter.addEventListener("change", filterRows);
}
