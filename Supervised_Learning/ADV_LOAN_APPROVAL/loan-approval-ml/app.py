import streamlit as st
import requests

st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦"
)

st.title("🏦 Loan Approval Predictor")
st.write("Enter the applicant details below.")

# Applicant details
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])

applicant_income = st.number_input(
    "Applicant Income", min_value=0.0, value=5000.0
)

coapplicant_income = st.number_input(
    "Coapplicant Income", min_value=0.0, value=0.0
)

loan_amount = st.number_input(
    "Loan Amount", min_value=0.0, value=150.0
)

loan_term = st.selectbox(
    "Loan Amount Term",
    [360, 180, 120, 84, 60, 36, 12]
)

credit_history = st.selectbox(
    "Credit History",
    [1.0, 0.0]
)

property_area = st.selectbox(
    "Property Area",
    ["Urban", "Semiurban", "Rural"]
)

if st.button("Predict Loan Approval"):

    data = {
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Property_Area": property_area
    }

    try:
        response = requests.post(
            "https://YOUR-FASTAPI-URL/predict",
            json=data
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
            st.error("API Error")
            st.write(response.text)

    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to FastAPI. Make sure the backend is running.")
