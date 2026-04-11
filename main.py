from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="SureScore Underwriting API")

# Define expected data structures
class ApplicantData(BaseModel):
    full_name: str
    dob: str
    bmi: float
    smoking: str
    alcohol: str
    activity: str

@app.post("/api/v1/extract-documents")
async def extract_documents(file: UploadFile = File(...)):
    # TODO: Integrate Langflow/OCR agent here to parse PDFs
    # For now, returning mock extracted data
    return {
        "status": "success",
        "extracted_data": {
            "income": 85000,
            "pre_existing_conditions": "none"
        }
    }

@app.post("/api/v1/predict-risk")
async def predict_risk(data: ApplicantData):
    # TODO: Pass data to XGBoost model and generate SHAP values
    # Expected output structure for the frontend
    return {
        "risk_score": 40,
        "risk_level": "Low",
        "premium_estimate": 248,
        "shap_explanations": [
            {"feature": "Smoking", "impact": "-18%", "type": "positive"},
            {"feature": "BMI", "impact": "+12%", "type": "negative"}
        ]
    }

@app.post("/api/v1/generate-policy")
async def generate_policy(applicant_id: str):
    # TODO: Trigger LLM via Langchain to draft the final policy document
    return {"status": "Policy drafted successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
