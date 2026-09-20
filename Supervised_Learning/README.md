# Advanced Loan Approval – Supervised Machine Learning

## Project Description

Advanced Loan Approval is a machine learning-based application that predicts whether a loan application will be **Approved** or **Not Approved** based on applicant and loan-related information.

The system takes applicant details such as income, education, employment status, credit history, loan amount, loan term, and property area as input and generates a loan approval prediction along with its probability.

## Solution

The project follows a complete machine learning and application pipeline:

1. The cleaned loan dataset is used for model development.
2. Categorical features are encoded using `OneHotEncoder`.
3. Numerical features are scaled using `StandardScaler`.
4. Three classification models are trained:
   - Logistic Regression
   - Decision Tree
   - Random Forest
5. The models are evaluated using Accuracy, Precision, Recall, and F1 Score.
6. Logistic Regression was selected as the final model based on the current test results.
7. The complete preprocessing and trained model pipeline is saved as a `.pkl` file.
8. A FastAPI backend loads the saved pipeline and provides a loan prediction API.
9. A Streamlit web interface allows users to enter applicant details.
10. The Streamlit frontend communicates with the FastAPI backend and displays the final prediction and approval probability.

### Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 86.18% | 84.00% | 98.82% | 90.81% |
| Decision Tree | 75.61% | 82.35% | 82.35% | 82.35% |
| Random Forest | 82.11% | 84.62% | 90.59% | 87.50% |


## How to Run

### 1. Install Dependencies

Open a terminal in the `loan-approval-ml` directory and run:

### 2. Start the FastAPI Backend
python -m uvicorn main:app --reload

The API will be available at: 	http://127.0.0.1:8000
Swagger API documentation:		http://127.0.0.1:8000/docs

### 3. Start the Streamlit Frontend

Open a new terminal while keeping FastAPI running:
python -m streamlit run app.py

The application will be available at http://localhost:8501
