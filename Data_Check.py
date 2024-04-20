import pandas as pd


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
        "age": lambda x: x >= 0,
        # Add more checks for other columns as needed
    }

    # Check value ranges
    for column, check_func in value_checks.items():
        if (df[column].apply(check_func)).all():
            print(f"All values in column '{column}' are within expected range.")
        else:
            print(f"Warning: Values in column '{column}' are outside expected range.")


def cross_field_validation(df):
    # Example: Check if graduation year is after birth year
    if (df["graduation_year"] < df["birth_year"]).any():
        print("Warning: Graduation year is before birth year in some records.")


def data_integrity_checks(df1, df2):
    # Example: Check if foreign key relationship is maintained
    if not df1["student_id"].isin(df2["student_id"]).all():
        print("Warning: Foreign key relationship between DataFrames is violated.")


def duplicate_data_checks(df):
    # Check for duplicate rows
    duplicates = df.duplicated()
    if duplicates.any():
        print("Warning: Duplicate rows found!")
        print(df[duplicates])


# Example usage
if __name__ == "__main__":
    # Load your DataFrame
    df = pd.read_csv(r"C:\Users\rahul\Videos\covid19.csv")

    # Run checks
    data_consistency_checks(df)
    value_range_checks(df)
    cross_field_validation(df)
    duplicate_data_checks(df)
