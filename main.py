from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="SureScore AI Underwriting API")

class ApplicantData(BaseModel):
    name: str
    age: int
    income: float

@app.get("/")
def home():
    return {"status": "AI Underwriting Co-Pilot Active"}

@app.post("/assess-risk")
async def assess_risk(data: ApplicantData):
    # This is where Langflow would be triggered to orchestrate:
    # 1. Data Extraction (from unstructured inputs) [cite: 52]
    # 2. Risk Prediction (XGBoost) [cite: 53, 71]
    # 3. Explainability (SHAP) [cite: 73]
    
    # Placeholder logic for demonstration
    risk_score = 24  # Example output from XGBoost model
    explanation = "Income-to-age ratio indicates stability."
    
    return {
        "risk_score": risk_score,
        "status": "Low Risk",
        "explanation": explanation,
        "suggested_premium": 248.00
    }

@app.post("/upload-documents")
async def upload_docs(file: File(...)):
    # Connects to Data Extraction Agent [cite: 52]
    return {"filename": file.filename, "status": "Parsing Unstructured Data..."}
    from fastapi.middleware.cors import CORSMiddleware

# ... (rest of your FastAPI code)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with your frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
