import streamlit as st
import requests
import os


# Page configuration
st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦"
)


# Title
st.title("🏦 Loan Approval Predictor")
st.write("Enter the applicant details below.")


# Local FastAPI backend URL
API_URL = os.getenv("LOAN_APPROVAL_API_URL", "http://127.0.0.1:8001") + "/predict"


# Input fields
income = st.number_input(
    "Income",
    min_value=0.0,
    value=50000.0
)

credit_score = st.number_input(
    "Credit Score",
    min_value=0.0,
    max_value=850.0,
    value=700.0
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0.0,
    value=20000.0
)

employment_years = st.number_input(
    "Employment Years",
    min_value=0.0,
    value=5.0
)


# Prediction
if st.button("Predict Loan Approval"):

    data = {
        "income": income,
        "credit_score": credit_score,
        "loan_amount": loan_amount,
        "employment_years": employment_years,
    }

    try:
        response = requests.post(
            API_URL,
            json=data,
            timeout=30
        )

        if response.status_code == 200:

            result = response.json()

            st.subheader("Prediction Result")

            if result["prediction"] == "Approved":
                st.success("✅ Loan Approved")
            else:
                st.error("❌ Loan Not Approved")

            st.write(
                f"Approval Probability: "
                f"{result['approval_probability'] * 100:.2f}%"
            )

        else:
            st.error(f"API Error: {response.status_code}")
            st.write("Response:", response.text)

    except requests.exceptions.ConnectionError:
        st.error(
            "Cannot connect to FastAPI. "
            "Please start the backend server first."
        )

    except requests.exceptions.Timeout:
        st.error(
            "The backend did not respond in time."
        )

    except Exception as e:
        st.error(f"Unexpected error: {e}")


