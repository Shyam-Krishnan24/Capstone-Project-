# Advanced Loan Approval Prediction

This project predicts whether a loan application will be approved from income,
credit score, loan amount, and employment years.

## Project Contents

- `ADV_LOAN_APPROVAL/analysis/`: exploratory analysis notebook
- `ADV_LOAN_APPROVAL/data/loans.csv`: loan dataset
- `ADV_LOAN_APPROVAL/loan-approval-ml/main.py`: FastAPI backend
- `ADV_LOAN_APPROVAL/loan-approval-ml/app.py`: Streamlit frontend
- `ADV_LOAN_APPROVAL/loan-approval-ml/models/`: saved model files

## Input Ranges

| Input | Minimum | Maximum |
|---|---:|---:|
| Income | 20,206 | 149,981 |
| Credit score | 300 | 849 |
| Loan amount | 5,097 | 49,976 |
| Employment years | 0 | 19 |

## Setup

Open PowerShell in the `loan-approval-ml` directory:

```powershell
cd "Supervised_Learning\ADV_LOAN_APPROVAL\loan-approval-ml"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If the virtual environment already exists, only activate it and continue.

## Run the Backend

Open Terminal 1 and run:

```powershell
cd "Supervised_Learning\ADV_LOAN_APPROVAL\loan-approval-ml"
.\.venv\Scripts\Activate.ps1
python -m uvicorn main:app --reload --port 8001
```

The backend runs at `http://127.0.0.1:8001`.

## Run the Frontend

Keep the backend running. Open Terminal 2 and run:

```powershell
cd "Supervised_Learning\ADV_LOAN_APPROVAL\loan-approval-ml"
.\.venv\Scripts\Activate.ps1
streamlit run app.py --server.port 8501
```

Open `http://localhost:8501` in a browser.

## Test Values

Enter the following values into the four frontend fields.

| Test | Income | Credit score | Loan amount | Employment years | Expected result |
|---|---:|---:|---:|---:|---|
| Strong applicant | 120,000 | 800 | 15,000 | 15 | Approved |
| Moderate applicant | 50,000 | 700 | 20,000 | 5 | Approved |
| Weak applicant | 20,206 | 300 | 49,976 | 0 | Not Approved |

Select **Predict Loan Approval** after entering each row. The frontend should
display the decision and approval probability.

## Stop the Project

Press `Ctrl+C` in both terminals when testing is complete.