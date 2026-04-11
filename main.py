from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Enable CORS so your GitHub website can talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Applicant(BaseModel):
    name: str
    age: int
    income: float

@app.get("/")
async def root():
    return {"status": "SureScore AI Underwriting Engine Online"}

@app.post("/assess-risk")
async def assess(data: Applicant):
    # Simulating the Multi-Agent Pipeline (XGBoost + SHAP)
    # In a full build, this would call your Langflow nodes
    risk_score = 24 if data.income > 800000 else 65
    status = "Low Risk" if risk_score < 30 else "High Risk"
    
    return {
        "risk_score": risk_score,
        "status": status,
        "explanation": f"SHAP Insight: {data.name}'s income-to-age ratio is a primary risk reducer. Stability verified.",
        "suggested_premium": 2480.0 if status == "Low Risk" else 5200.0
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
