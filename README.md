
# Bank Loan Prediction

## 1. Project Overview

This project aims to develop a Machine Learning system capable of predicting whether a bank loan application is likely to be approved or rejected.

The project follows an end-to-end Data Science workflow, starting from data collection and exploration to model development and web deployment.

## 2. Business Problem

Banks receive many loan applications and must evaluate the financial and personal characteristics of applicants before making lending decisions.

The main objective is to use historical loan application data to identify patterns and build a classification model that predicts the loan status of new applicants.

## 3. Project Objectives

- Collect and understand the dataset.
- Clean and preprocess the data.
- Perform Exploratory Data Analysis (EDA).
- Identify relevant features.
- Train and compare Machine Learning models.
- Evaluate model performance.
- Deploy the selected model using Flask.

## 4. Dataset

Source: Kaggle

Dataset: Loan Prediction Dataset

Target variable: `Loan_Status`

- Y: Loan approved
- N: Loan rejected

## 5. Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Flask
- Jupyter Notebook
- Git and GitHub

## 6. Project Structure

```text
bank-loan-prediction-v2/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
├── models/
├── app/
│   ├── templates/
│   └── static/
├── docs/
├── requirements.txt
├── .gitignore
└── README.md
```

## 7. Project Workflow

1. Business Understanding
2. Data Collection
3. Data Understanding
4. Data Cleaning
5. Exploratory Data Analysis
6. Feature Engineering
7. Machine Learning
8. Model Evaluation
9. Deployment with Flask

## 8. Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd bank-loan-prediction-v2
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 9. Project Status

Currently working on data understanding, cleaning and exploratory data analysis.

## 10. Disclaimer

This project is developed for educational purposes. Its predictions are not intended to replace professional banking decisions or credit risk assessments.
