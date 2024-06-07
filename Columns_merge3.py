import pandas as pd
import csv
from io import StringIO

# Function to merge excess columns
def merge_excess_columns(row, expected_columns):
    if len(row) > expected_columns:
        row[expected_columns - 1] = '^'.join(row[expected_columns - 1:])
        del row[expected_columns:]  # Remove excess columns
    return row

# Read the CSV file as raw text
with open('your_file.csv', 'r') as file:
    content = file.read()

# Use csv.reader to parse the content
data = []
reader = csv.reader(StringIO(content), delimiter='^')

# Extract column names from the first row
column_names = next(reader)

# Process each row to handle excess columns
for row in reader:
    row = merge_excess_columns(row, 54)
    data.append(row)

# Convert the processed data back into a DataFrame
df = pd.DataFrame(data)

# Assign extracted column names to DataFrame columns
df.columns = column_names

# Print the first few rows to verify
print(df.head())
