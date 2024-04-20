import pandas as pd

def check_dataframe(df):
    """
    Check if DataFrame has correct columns and data types.

    Parameters:
    df (DataFrame): Input DataFrame.

    Returns:
    bool: True if DataFrame is valid, False otherwise.
    """
    expected_columns = ['A', 'B']
    if list(df.columns) != expected_columns:
        return False
    
    # Check data types
    if not all(df.dtypes == int):
        return False
    
    return True

# Example usage
df = pd.DataFrame({'A': [1, 2, 3, 4],
                   'B': [5, 6, 7, 8]})
print(check_dataframe(df))  # Output: True
