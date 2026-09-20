# Advanced Loan Approval Prediction

## Project Description

Advanced Loan Approval Prediction is a supervised machine learning project that predicts whether a loan application is likely to be approved based on an applicant's financial and employment information.

The project implements a complete machine learning workflow, from data analysis and preprocessing to model training, evaluation, API development, and web application deployment.

---

## Dataset

The project uses the `loans.csv` dataset containing **1,000 loan application records** and **5 columns**.

### Features

| Feature | Description | Minimum | Maximum |
|---|---|---:|---:|
| `income` | Applicant income | 20,206 | 149,981 |
| `credit_score` | Applicant credit score | 300 | 849 |
| `loan_amount` | Requested loan amount | 5,097 | 49,976 |
| `employment_years` | Applicant employment duration | 0 | 19 |

### Target Variable

| Target | Description | Values |
|---|---|---|
| `loan_status` | Loan approval status | `0` = Not Approved, `1` = Approved |

### Input Value Ranges

For prediction, the application accepts values within the ranges observed in the dataset:

```text
Income             : 20,206 – 149,981
Credit Score       : 300 – 849
Loan Amount        : 5,097 – 49,976
Employment Years   : 0 – 19

## Models Used

The following supervised machine learning algorithms are trained and evaluated:

1. Logistic Regression
2. Decision Tree
3. Random Forest

### Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 99.50% | 99.01% | 100.00% | 99.50% |
| Decision Tree | 94.50% | 94.95% | 94.00% | 94.47% |
| Random Forest | 97.00% | 97.00% | 97.00% | 97.00% |