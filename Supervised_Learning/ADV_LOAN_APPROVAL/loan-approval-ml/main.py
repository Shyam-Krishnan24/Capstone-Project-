from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from pathlib import Path

app = FastAPI(title="Loan Approval Prediction API")

MODEL_PATH = Path(__file__).parent / "models" / "loan_approval_model.pkl"
model = joblib.load(MODEL_PATH)


class LoanApplicant(BaseModel):
    income: float
    credit_score: float
    loan_amount: float
    employment_years: float


@app.get("/")
def home():
    return {"message": "Loan Approval API is running"}


@app.post("/predict")
def predict(applicant: LoanApplicant):
    data = pd.DataFrame([applicant.model_dump()])
    prediction = model.predict(data)[0]
    probabilities = model.predict_proba(data)[0]
    approval_probability = float(probabilities[1])

    result = "Approved" if prediction == 1 else "Not Approved"

    return {
        "prediction": result,
        "approval_probability": round(approval_probability, 4),
        "decision": int(prediction),
    }
    