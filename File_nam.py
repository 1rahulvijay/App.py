import os
import pandas as pd

# Directory containing the files
directory = '/path/to/your/directory'

# List of target filenames
target_filenames = ['abc.xlsx', 'dbg.xlsx']

# List all files in the directory
files_in_directory = os.listdir(directory)

# Check for each target file and read it if it exists
for target_filename in target_filenames:
    if target_filename in files_in_directory:
        # Construct the full path to the file
        file_path = os.path.join(directory, target_filename)
        
        # Read the Excel file
        df = pd.read_excel(file_path)
        
        # Display the filename and the dataframe
        print(f"Contents of {target_filename}:")
        print(df)
    else:
        print(f"File '{target_filename}' not found in the directory.")
