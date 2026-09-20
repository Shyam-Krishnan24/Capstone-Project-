from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from pathlib import Path

app = FastAPI(title="Loan Approval Prediction API")

# Load trained ML pipeline
MODEL_PATH = Path(__file__).parent / "models" / "loan_approval_model.pkl"
model = joblib.load(MODEL_PATH)


# Input structure
class LoanApplicant(BaseModel):
    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: str


@app.get("/")
def home():
    return {"message": "Loan Approval API is running"}


@app.post("/predict")
def predict(applicant: LoanApplicant):

    data = pd.DataFrame([applicant.model_dump()])

    prediction = model.predict(data)[0]

    # Get probability if supported
    probabilities = model.predict_proba(data)[0]
    approval_probability = float(probabilities[1])

    result = "Approved" if prediction == "Y" else "Not Approved"

    return {
        "prediction": result,
        "approval_probability": round(approval_probability, 4)
    }
    