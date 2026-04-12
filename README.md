# SureScore | AI Underwriting Co-Pilot 🏥

[cite_start]This repository contains the **Risk Assessment Agent** for SureScore, a multi-agent system designed to automate insurance underwriting[cite: 32, 40].

## 🧠 Model Specifications
- [cite_start]**Algorithm**: XGBoost (Extreme Gradient Boosting)[cite: 35, 57].
- [cite_start]**Explainability**: SHAP (Shapley Additive exPlanations) for mandatory audit trails[cite: 27, 57].
- [cite_start]**Domain**: Healthcare Insurance[cite: 16].

## 📊 Impact & Value
- [cite_start]**Time Saving**: Reduces underwriting time from days to under 5 minutes[cite: 87, 131].
- [cite_start]**Cost Efficiency**: Reduces manual underwriting costs by 60-70%[cite: 87, 126].
- [cite_start]**Human-in-the-Loop**: Specifically trained to handle missing data (like Ramesh Kulkarni's BMI) by alerting underwriters for final approval[cite: 39, 215].

## 🛠️ Usage
[cite_start]The `.pkl` models are designed to be loaded into a **FastAPI** backend and orchestrated via **Langflow** nodes[cite: 43, 46].
