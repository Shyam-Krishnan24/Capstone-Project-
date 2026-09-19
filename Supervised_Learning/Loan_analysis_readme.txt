#Reference Notes done while Data Handling:

------------------------------------------

Applicant Income Analysis: The applicant income distribution is positively/right-skewed, with most observations concentrated at lower income levels and a long right tail containing relatively high-income observations. The mean income (5,403.46) is higher than the median (3,812.50), which is consistent with the right-skewed distribution. Extreme observations should be investigated further rather than automatically removed

Loan Amount Analysis: The loan amount distribution is positively skewed. Most applications have loan amounts concentrated around the lower-to-middle range, while a smaller number of applications have substantially larger loan amounts. The mean loan amount (146.41) is higher than the median (128), consistent with the right-skewed distribution.

Coapplicant Income Analysis: The coapplicant income variable has 614 non-missing observations. At least 25% of applicants have zero coapplicant income. The mean (1,621.25) is higher than the median (1,188.50), indicating a right-skewed distribution. The maximum value of 41,667 is substantially higher than the typical values and warrants further outlier investigation.

Coapplicant Income Analysis: The distribution is strongly right-skewed, with a substantial number of applicants having zero coapplicant income. Most non-zero values are concentrated at relatively lower income levels, while a small number of observations have substantially higher values

Loan Amount Term Analysis: The loan-term variable is highly concentrated at 360 months, with 512 of the 614 observations having this term. Other loan terms occur considerably less frequently. This indicates low variation in the variable, with 360 months being the dominant repayment period in the dataset.

Loan Amount Term Analysis: The loan-term distribution is highly concentrated at 360 months. Out of 614 applications, 512 have a 360-month term, while all other terms occur substantially less frequently. Fourteen observations are missing. This indicates limited variation in the loan-term variable

Credit History Analysis: A strong association was observed between credit history and loan approval in the dataset. Among applicants with a credit-history value of 1, 79.58% were approved, whereas only 7.87% of applicants with a value of 0 were approved. The missing-credit-history group had a 74.00% approval rate. This suggests that credit history is an important variable to investigate further during supervised-learning model development.

Gender vs Loan Approval: The loan approval proportions were similar for male and female applicants. Approximately 69.33% of male applicants and 66.96% of female applicants were approved. The relatively small difference suggests a weaker association between gender and loan approval in this dataset compared with variables such as credit history.

Marital Status vs Loan Approval: Married applicants had an observed approval proportion of 71.61%, compared with 62.91% among applicants who were not married. This represents an 8.70 percentage-point difference in approval proportions between the two groups.

Dependents Analysis: Most applicants have no dependents (345), followed by applicants with one dependent (102), two dependents (101), and three or more dependents (51). There are 15 missing observations. Loan approval proportions were relatively similar across the dependent categories, ranging from 64.71% to 75.25%.

Applicant Income vs Loan Approval: The mean applicant income was 5,446.08 for rejected applications and 5,384.07 for approved applications. The median incomes were also similar at 3,833.50 and 3,812.50 respectively. Therefore, the descriptive statistics show only a small difference in applicant income between the two loan-status groups.

Coapplicant Income vs Loan Approval: Both loan-status groups contain substantial outliers. The rejected group has particularly extreme coapplicant-income observations, causing its mean to be considerably higher than its median. Therefore, median and distribution-based analysis should be considered alongside the mean when interpreting this variable.

Loan Amount vs Loan Approval: The mean loan amount was 151.22 for rejected applications and 144.29 for approved applications. The median values were 129 and 126 respectively. The relatively similar distributions indicate only a small difference in typical loan amounts between the two loan-status groups, although some extreme loan amounts are present.

Loan Amount vs Loan Approval: The distributions of loan amounts for approved and rejected applications are broadly similar, with median values of 126 and 129 respectively. Both groups contain several high-value observations that appear as outliers. Therefore, loan amount shows only a modest difference between the two loan-status groups in this dataset.

Correlation Analysis: The correlation analysis shows that ApplicantIncome and LoanAmount have the strongest numerical relationship, with a correlation coefficient of 0.57, indicating a moderate positive linear association. CoapplicantIncome and LoanAmount show a weak positive correlation of 0.19, while the remaining numerical variable pairs exhibit weak or near-zero linear relationships.	