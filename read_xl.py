import pandas as pd
import os

def read_excel_file(file_path):
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found.")
        
        # Attempt to read the Excel file
        df = pd.read_excel(file_path)
        
        # If successful, return the DataFrame
        return df
    except FileNotFoundError as e:
        print(e)
        return None
    except pd.errors.ParserError as e:
        print(f"Error parsing Excel file '{file_path}': {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage:
file_path = "example.xlsx"  # Change to your file path
data = read_excel_file(file_path)
if data is not None:
    print("Data loaded successfully!")
    print(data.head())
else:
    print("Failed to load data. Please check the file path and try again.")
