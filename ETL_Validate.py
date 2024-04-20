import pandas as pd

# Load the source data
source_data = pd.read_csv('source_data.csv')

# Load the transformed data
transformed_data = pd.read_csv('transformed_data.csv')

# Perform basic data validation
def validate_data(source_data, transformed_data):
    # Check if the number of rows is the same
    if len(source_data) != len(transformed_data):
        print("Number of rows doesn't match!")
        return False
    
    # Check if columns are the same
    if list(source_data.columns) != list(transformed_data.columns):
        print("Columns don't match!")
        return False
    
    # Check for any missing values
    if source_data.isnull().values.any() or transformed_data.isnull().values.any():
        print("Missing values detected!")
        return False
    
    # Check for data type consistency (optional)
    # You can add additional checks depending on your specific data requirements
    
    return True

# Perform data validation
if validate_data(source_data, transformed_data):
    print("Data validation passed successfully!")
else:
    print("Data validation failed!")
