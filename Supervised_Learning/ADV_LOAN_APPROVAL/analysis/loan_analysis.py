import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"C:\Users\harivarman\Desktop\adv loan approval project\data\Loan_Data.csv")
print("shape: ", df.shape)
print("\n column name:")
print(df.columns.tolist())
print("\nfirst few data")
print(df.head(10).to_string())
print("\nDB info:")
print(df.info)
print("\n missing values:")
print(df.isnull().sum())
print("\nDuplicate Rows:")
print(df.duplicated().sum())
print("\n ----------Loan status analysis---------------")
print("\nLoan Status Count:")
print(df["Loan_Status"].value_counts())
print("\nLoan Status Percentage:")
print(
    df["Loan_Status"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)
plt.figure(figsize=(6, 4))

sns.countplot(
    data=df,
    x="Loan_Status"
)

plt.title("Loan Approval Distribution")
plt.xlabel("Loan Status")
plt.ylabel("Number of Applicants")

plt.tight_layout()
plt.show()
print("\n ---------------applicants income analysis--------------- ")
print(df["ApplicantIncome"].describe())
plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="ApplicantIncome",
    kde=True
)

plt.title("Applicant Income Distribution")
plt.xlabel("Applicant Income")
plt.ylabel("Number of Applicants")

plt.tight_layout()
plt.show()
print("\n -----------loan amount analysis------------------------")
print(df["LoanAmount"].describe())
plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="LoanAmount",
    kde=True
)

plt.title("Loan Amount Distribution")
plt.xlabel("Loan Amount")
plt.ylabel("Number of Applicants")

plt.tight_layout()
plt.show()
print("\n ------------------coappliant income analysis--------------------")
print(df["CoapplicantIncome"].describe())
plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="CoapplicantIncome",
    kde=True
)

plt.title("Coapplicant Income Distribution")
plt.xlabel("Coapplicant Income")
plt.ylabel("Number of Applicants")

plt.tight_layout()
plt.show()
print("\n-------------- Loan amount term analysis -------------")
print(df["Loan_Amount_Term"].describe())
print("\nLoan Amount Term Frequency:")
print(df["Loan_Amount_Term"].value_counts().sort_index())
plt.figure(figsize=(9, 5))

sns.countplot(
    data=df,
    x="Loan_Amount_Term"
)

plt.title("Loan Amount Term Distribution")
plt.xlabel("Loan Amount Term (Months)")
plt.ylabel("Number of Applicants")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
print("\n------------- credit history analysis ----------------")
print("Credit History Frequency:")
print(df["Credit_History"].value_counts(dropna=False))
print("\nCredit History vs Loan Status:")

print(
    pd.crosstab(
        df["Credit_History"],
        df["Loan_Status"],
        dropna=False
    )
)
print("\nLoan Approval Percentage by Credit History:")
print(
    pd.crosstab(
        df["Credit_History"],
        df["Loan_Status"],
        normalize="index",
        dropna=False
    ).mul(100).round(2)
)
plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="Credit_History",
    hue="Loan_Status"
)

plt.title("Credit History vs Loan Approval")
plt.xlabel("Credit History")
plt.ylabel("Number of Applicants")

plt.tight_layout()
plt.show()
print("\n --------------------education vs loan status--------------------")
print(
    pd.crosstab(
        df["Education"],
        df["Loan_Status"]
    )
)
print("\nLoan Approval Percentage by Education:")
print(
    pd.crosstab(
        df["Education"],
        df["Loan_Status"],
        normalize="index"
    ).mul(100).round(2)
)
plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="Education",
    hue="Loan_Status"
)

plt.title("Education vs Loan Approval")
plt.xlabel("Education")
plt.ylabel("Number of Applicants")

plt.tight_layout()
plt.show()
print("\n----------- property area vs loan status-----------------")
print(
    pd.crosstab(
        df["Property_Area"],
        df["Loan_Status"]
    )
)
print("\nLoan Approval Percentage by Property Area:")
print(
    pd.crosstab(
        df["Property_Area"],
        df["Loan_Status"],
        normalize="index"
    ).mul(100).round(2)
)
plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="Property_Area",
    hue="Loan_Status"
)

plt.title("Property Area vs Loan Approval")
plt.xlabel("Property Area")
plt.ylabel("Number of Applicants")

plt.tight_layout()
plt.show()
print("\n------------Gender vs loan status--------------")
print(
    pd.crosstab(
        df["Gender"],
        df["Loan_Status"]
    )
)
print("\nLoan Approval Percentage by Gender:")
print(
    pd.crosstab(
        df["Gender"],
        df["Loan_Status"],
        normalize="index"
    ).mul(100).round(2)
)
plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="Gender",
    hue="Loan_Status"
)

plt.title("Gender vs Loan Approval")
plt.xlabel("Gender")
plt.ylabel("Number of Applicants")

plt.tight_layout()
plt.show()
print("\n----------------married vs loan status------------------")
print(
    pd.crosstab(
        df["Married"],
        df["Loan_Status"]
    )
)
print("\nLoan Approval Percentage by Marital Status:")
print(
    pd.crosstab(
        df["Married"],
        df["Loan_Status"],
        normalize="index"
    ).mul(100).round(2)
)
plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="Married",
    hue="Loan_Status"
)

plt.title("Marital Status vs Loan Approval")
plt.xlabel("Marital Status")
plt.ylabel("Number of Applicants")

plt.tight_layout()
plt.show()
print("\n========== DEPENDENTS VS LOAN STATUS ==========")

print(
    pd.crosstab(
        df["Dependents"],
        df["Loan_Status"]
    )
)

print("\nLoan Approval Percentage by Dependents:")

print(
    pd.crosstab(
        df["Dependents"],
        df["Loan_Status"],
        normalize="index"
    ).mul(100).round(2)
)
plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="Dependents",
    hue="Loan_Status"
)

plt.title("Dependents vs Loan Approval")
plt.xlabel("Number of Dependents")
plt.ylabel("Number of Applicants")

plt.tight_layout()
plt.show()
print("\nDependents including missing values:")
print(df["Dependents"].value_counts(dropna=False))
print("\n========== SELF EMPLOYED VS LOAN STATUS ==========")

print(
    pd.crosstab(
        df["Self_Employed"],
        df["Loan_Status"]
    )
)

print("\nLoan Approval Percentage by Self Employment:")

print(
    pd.crosstab(
        df["Self_Employed"],
        df["Loan_Status"],
        normalize="index"
    ).mul(100).round(2)
)
plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="Self_Employed",
    hue="Loan_Status"
)

plt.title("Self Employment vs Loan Approval")
plt.xlabel("Self Employed")
plt.ylabel("Number of Applicants")

plt.tight_layout()
plt.show()
print("\n========== APPLICANT INCOME VS LOAN STATUS ==========")

print(
    df.groupby("Loan_Status")["ApplicantIncome"].describe()
)
plt.figure(figsize=(7, 5))

sns.boxplot(
    data=df,
    x="Loan_Status",
    y="ApplicantIncome"
)

plt.title("Applicant Income vs Loan Approval")
plt.xlabel("Loan Status")
plt.ylabel("Applicant Income")

plt.tight_layout()
plt.show()
print("\n========== COAPPLICANT INCOME VS LOAN STATUS ==========")

print(
    df.groupby("Loan_Status")["CoapplicantIncome"].describe()
)
plt.figure(figsize=(7, 5))

sns.boxplot(
    data=df,
    x="Loan_Status",
    y="CoapplicantIncome"
)

plt.title("Coapplicant Income vs Loan Approval")
plt.xlabel("Loan Status")
plt.ylabel("Coapplicant Income")

plt.tight_layout()
plt.show()
print("\n========== LOAN AMOUNT VS LOAN STATUS ==========")

print(
    df.groupby("Loan_Status")["LoanAmount"].describe()
)
plt.figure(figsize=(7, 5))

sns.boxplot(
    data=df,
    x="Loan_Status",
    y="LoanAmount"
)

plt.title("Loan Amount vs Loan Approval")
plt.xlabel("Loan Status")
plt.ylabel("Loan Amount")

plt.tight_layout()
plt.show()
print("\n========== OUTLIER ANALYSIS ==========")

numerical_columns = [
    "ApplicantIncome",
    "CoapplicantIncome",
    "LoanAmount"
]

for column in numerical_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ]

    print(f"\n{column}")
    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)
    print("Lower Bound:", lower_bound)
    print("Upper Bound:", upper_bound)
    print("Number of Outliers:", len(outliers))
print("\n========== CORRELATION ANALYSIS ==========")

numeric_columns = [
    "ApplicantIncome",
    "CoapplicantIncome",
    "LoanAmount",
    "Loan_Amount_Term",
    "Credit_History"
]

correlation_matrix = df[numeric_columns].corr()

print(correlation_matrix)
plt.figure(figsize=(9, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap of Numerical Variables")
plt.tight_layout()
plt.show()

print("\n========== FINAL MISSING VALUE SUMMARY ==========")

missing = df.isnull().sum()

missing_percentage = (
    df.isnull().mean() * 100
).round(2)

missing_summary = pd.DataFrame({
    "Missing Count": missing,
    "Missing Percentage": missing_percentage
})

print(missing_summary)