
# 03 - Data Cleaning

## 1. Objective

Prepare the raw dataset by identifying and handling missing values, duplicates and inconsistent data.

## 2. Missing Values

Missing values are identified using:

```python
df.isnull().sum()
```

## 3. Duplicate Detection

```python
df.duplicated().sum()
```

## 4. Data Types

```python
df.dtypes
```

## 5. Missing Value Treatment

Categorical and numerical variables require different treatment strategies.

The selected imputation methods must be justified according to the meaning and distribution of each variable.

## 6. Validation

Verify that the final dataset contains no unexpected missing values or duplicates.

## 7. Important Consideration

The final preprocessing strategy must avoid data leakage by learning imputation and encoding parameters only from training data.
