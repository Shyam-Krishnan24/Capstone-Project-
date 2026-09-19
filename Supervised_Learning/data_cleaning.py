import pandas as pd

df = pd.read_csv("data/loan_data.csv")
print("Original dataset shape:", df.shape)

df_clean = df.copy()

df_clean = df_clean.drop(columns=["Loan_ID"])

print("\nDuplicate rows:")
print(df_clean.duplicated().sum())
df_clean["Gender"] = df_clean["Gender"].fillna(df_clean["Gender"].mode()[0])
df_clean["Married"] = df_clean["Married"].fillna(df_clean["Married"].mode()[0])
df_clean["Dependents"] = df_clean["Dependents"].fillna(df_clean["Dependents"].mode()[0])
df_clean["Self_Employed"] = df_clean["Self_Employed"].fillna(df_clean["Self_Employed"].mode()[0])

df_clean["LoanAmount"] = df_clean["LoanAmount"].fillna(df_clean["LoanAmount"].median())
df_clean["Loan_Amount_Term"] = df_clean["Loan_Amount_Term"].fillna(df_clean["Loan_Amount_Term"].median())

df_clean["Credit_History"] = df_clean["Credit_History"].fillna(df_clean["Credit_History"].mode()[0])

print("\nMissing values after cleaning:")
print(df_clean.isnull().sum())
df_clean.to_csv("data/cleaned_loan_data.csv", index=False)

print("\nCleaned dataset shape:", df_clean.shape)
print("Cleaned dataset saved successfully.")