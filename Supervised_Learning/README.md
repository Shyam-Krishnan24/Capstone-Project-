Project: Advanced Loan Approval – Supervised ML

Completed so far:

1. Harivarman completed the data cleaning and prepared the cleaned dataset:
	data/cleaned_loan_data.csv

2. Shyaam completed the ML development:
	- Train/test split (80/20, stratified)
	- Categorical feature encoding using OneHotEncoder
	- Numerical feature scaling using StandardScaler
	- Trained Logistic Regression
	- Trained Decision Tree
	- Trained Random Forest
	- Compared Accuracy, Precision, Recall and F1 Score
	- Generated confusion matrices
	- Generated classification report
	- Logistic Regression was selected as the final model based on the current test results
	- Saved the complete preprocessing + ML pipeline as:
	  models/loan_approval_model.pkl

Current ML results:
- Logistic Regression: Accuracy 86.18%, Precision 84.00%, Recall 98.82%, F1 90.81%
- Decision Tree: Accuracy 75.61%, Precision 82.35%, Recall 82.35%, F1 82.35%
- Random Forest: Accuracy 82.11%, Precision 84.62%, Recall 90.59%, F1 87.50%

Harini's remaining work:

1. Build the FastAPI backend.
2. Load models/loan_approval_model.pkl.
3. Create an API endpoint for loan prediction.
4. Accept all required applicant inputs through the API.
5. Pass the input directly to the saved ML pipeline.
6. Return the predicted Loan_Status and prediction probability.
7. Build the web frontend for entering applicant details.
8. Connect the frontend to the FastAPI backend.
9. Display the final loan approval result clearly.
10. Perform API, frontend and end-to-end testing.

Important:
Do NOT retrain or recreate the ML preprocessing/model.
Use the existing saved pipeline:
models/loan_approval_model.pkl

Maintain the existing project structure and build the backend/frontend around the completed ML pipeline.
