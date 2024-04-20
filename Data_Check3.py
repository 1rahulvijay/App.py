import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def data_consistency_checks(df):
    # Check for missing values
    missing_values = df.isnull().sum()
    if missing_values.sum() > 0:
        print("Warning: Missing values found!")
        print(missing_values)

    # Check data types
    print("Data Types:")
    print(df.dtypes)

def value_range_checks(df):
    # Define value range checks for specific columns
    value_checks = {
        'total_cases': lambda x: x >= 0,
        'new_cases': lambda x: x >= 0,
        'total_deaths': lambda x: x >= 0,
        'new_deaths': lambda x: x >= 0,
        # Add more checks for other columns as needed
    }

    # Check value ranges
    for column, check_func in value_checks.items():
        if (df[column].apply(check_func)).all():
            print(f"All values in column '{column}' are within expected range.")
        else:
            print(f"Warning: Values in column '{column}' are outside expected range.")

def cross_field_validation(df):
    # Example: Check if total cases are greater than or equal to new cases
    if (df['total_cases'] < df['new_cases']).any():
        print("Warning: Total cases is less than new cases in some records.")

def outlier_detection(df):
    # Detect outliers using Tukey's method
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    outliers = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).sum()
    if outliers.sum() > 0:
        print("Warning: Outliers detected!")
        print(outliers)

def data_distribution_analysis(df):
    # Visualize data distributions
    for column in df.columns:
        if df[column].dtype in ['int64', 'float64']:
            sns.histplot(df[column], kde=True)
            plt.title(f'Distribution of {column}')
            plt.show()

# Example usage
if __name__ == "__main__":
    # Load your DataFrame
    df = pd.read_csv(r"C:\Users\rahul\Videos\covid19.csv")

    # Run checks
    data_consistency_checks(df)
    value_range_checks(df)
    cross_field_validation(df)
    outlier_detection(df)
    data_distribution_analysis(df)
