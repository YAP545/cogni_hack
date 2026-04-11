from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# FIX 1: Enhanced CORS (Allows everything for development)
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
    # This simulates the Multi-Agent risk assessment from your PPT
    return {
        "risk_score": 24,
        "status": "Low Risk",
        "explanation": f"Analysis for {data.name} complete. High income-to-age stability detected.",
        "suggested_premium": 2480.0
    }

if __name__ == "__main__":
    # FIX 2: Bind to 0.0.0.0 to avoid IPv6/Localhost conflicts
    uvicorn.run(app, host="0.0.0.0", port=8000)
