from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CRITICAL: Allow your website to talk to your backend
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

@app.post("/assess-risk")
async def assess(data: Applicant):
    # Simulated Multi-Agent Logic [cite: 35, 43]
    # In a full build, this triggers Langflow agents [cite: 46]
    risk_score = 24 
    status = "Low Risk"
    explanation = "Stable income and age demographic lead to a low risk profile[cite: 103]."
    
    return {
        "risk_score": risk_score,
        "status": status,
        "explanation": explanation,
        "suggested_premium": 2480.0
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
