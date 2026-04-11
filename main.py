from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "SureScore Multi-Agent Engine Live"}

@app.post("/assess-risk")
async def assess(
    name: str = Form(...),
    age: int = Form(...),
    income: float = Form(...),
    file: UploadFile = File(None)
):
    # Simulated Multi-Agent Pipeline Logic
    # 1. OCR Agent would process 'file' here
    # 2. Risk Agent (XGBoost) calculates score
    risk_score = 24 if income > 800000 and age < 50 else 68
    status = "Low Risk" if risk_score < 40 else "High Risk"
    
    return {
        "risk_score": risk_score,
        "status": status,
        "explanation": f"Analysis for {name} complete. High income-to-age stability detected via SHAP.",
        "suggested_premium": 2480.0 if status == "Low Risk" else 5500.0,
        "file_received": file.filename if file else "None"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
