import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


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
        "total_cases": lambda x: x >= 0,
        "new_cases": lambda x: x >= 0,
        "total_deaths": lambda x: x >= 0,
        "new_deaths": lambda x: x >= 0,
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
    if (df["total_cases"] < df["new_cases"]).any():
        print("Warning: Total cases is less than new cases in some records.")


def outlier_detection(df):
    # Detect outliers using Tukey's method
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    df_aligned, IQR_aligned = df.align(IQR, axis=1, join='inner')  # Align DataFrame and Series
    df_aligned, Q1_aligned = df_aligned.align(Q1, axis=1, join='inner')  # Align DataFrame and Series
    df_aligned, Q3_aligned = df_aligned.align(Q3, axis=1, join='inner')  # Align DataFrame and Series
    outliers = ((df_aligned < (Q1_aligned - 1.5 * IQR_aligned)) | (df_aligned > (Q3_aligned + 1.5 * IQR_aligned))).sum()
    if outliers.sum() > 0:
        print("Warning: Outliers detected!")
        print(outliers)



def correlation_analysis(df):
    # Compute Pearson correlation coefficient and visualize correlations
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()


def trend_analysis(df):
    # Example: Compute and visualize trend of total cases over time
    plt.plot(df["date"], df["total_cases"], marker="o", linestyle="-")
    plt.title("Trend of Total Cases Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Cases")
    plt.xticks(rotation=45)
    plt.show()


def data_profiling(df):
    # Generate descriptive statistics and visualizations for each column
    for column in df.columns:
        print(f"Column: {column}")
        print(df[column].describe())
        if df[column].dtype in ["int64", "float64"]:
            sns.histplot(df[column], kde=True)
            plt.title(f"Distribution of {column}")
            plt.show()


# Example usage
if __name__ == "__main__":
    # Load your DataFrame
    df = pd.read_csv(r"C:\Users\rahul\Videos\covid19.csv")

    # Run checks and analyses
    data_consistency_checks(df)
    value_range_checks(df)
    cross_field_validation(df)
    outlier_detection(df)
    correlation_analysis(df)
    trend_analysis(df)
    data_profiling(df)
