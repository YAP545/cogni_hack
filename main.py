from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import asyncio

app = FastAPI(title="SureScore Underwriting API")

# VERY IMPORTANT: This allows your frontend to talk to your backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, change this to your GitHub Pages URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define what data the frontend will send us
class ApplicantData(BaseModel):
    bmi: float
    smoking: str
    alcohol: str
    activity: str
    insuranceType: str
    coverage: int

@app.post("/api/v1/extract-documents")
async def extract_documents(file: UploadFile = File(...)):
    # Simulate OCR processing time
    await asyncio.sleep(2) 
    
    # Return mock extracted data based on the file uploaded
    return {
        "status": "success",
        "filename": file.filename,
        "extracted_data": {
            "name": "Alex Johnson",
            "dob": "15 Mar 1990",
            "blood_group": "O+",
            "income": "$85,000"
        }
    }

@app.post("/api/v1/predict-risk")
async def predict_risk(data: ApplicantData):
    # Simulate AI Model Calculation time (XGBoost + SHAP)
    await asyncio.sleep(3)
    
    # Calculate a basic dynamic score based on frontend inputs for the demo
    base_score = 30
    if data.smoking == "smoker": base_score += 35
    if data.alcohol == "heavy": base_score += 15
    if data.bmi > 25: base_score += 10
    
    risk_level = "High" if base_score > 60 else "Medium" if base_score > 40 else "Low"
    premium = 150 + (base_score * 2.5)

    return {
        "status": "success",
        "risk_score": min(base_score, 100),
        "risk_level": risk_level,
        "premium_estimate": int(premium),
        "confidence": 94
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
