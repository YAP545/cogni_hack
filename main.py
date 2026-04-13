from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="SureScore AI API")

# VERY IMPORTANT: This allows your HTML file to communicate with the server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows requests from any web page
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Models
try:
    model = joblib.load('optimized_health_risk_model.pkl')
    encoder = joblib.load('health_label_encoder.pkl')
    print("✅ SureScore Brain Loaded Successfully!")
except Exception as e:
    print(f"⚠️ Error loading models: {e}")

# Define the expected inputs
class Applicant(BaseModel):
    age: int
    annual_income: float
    bmi: float
    is_smoker: int
    pre_existing_conditions: int
    glucose_level: float
    cholesterol: float

@app.post("/predict/health")
def predict_risk(applicant: Applicant):
    try:
        data = pd.DataFrame([applicant.dict()])
        
        # Predict Risk Level
        prediction = model.predict(data)
        risk_level = encoder.inverse_transform(prediction)[0]

        # Predict Risk Score
        probabilities = model.predict_proba(data)
        risk_score = round(max(probabilities[0]) * 100, 2)

        return {
            "prediction": {
                "risk_level": risk_level,
                "risk_score": f"{risk_score}"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
