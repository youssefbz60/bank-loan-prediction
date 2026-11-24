
# 02 - Data Collection

## 1. Data Source

Platform: Kaggle

Dataset: Loan Prediction Dataset

## 2. Collection Method

The dataset was downloaded from Kaggle and imported into Python using Pandas.

## 3. Data Loading

```python
df = pd.read_csv("data/raw/train.csv")
```

## 4. Variables

The dataset contains applicant information such as:

- Gender
- Married
- Dependents
- Education
- Self_Employed
- ApplicantIncome
- CoapplicantIncome
- LoanAmount
- Loan_Amount_Term
- Credit_History
- Property_Area

Target: Loan_Status

## 5. Notes

The dataset is used for educational and experimental purposes.
