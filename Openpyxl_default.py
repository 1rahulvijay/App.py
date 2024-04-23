import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import NamedStyle

# Create a Pandas DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Create an Excel writer object
excel_writer = pd.ExcelWriter('output.xlsx', engine='openpyxl')

# Write the DataFrame to Excel
df.to_excel(excel_writer, index=False, sheet_name='Sheet1')

# Get the workbook and default worksheet
workbook = excel_writer.book
worksheet = workbook.active

# Define a default style
default_style = NamedStyle(name='default')

# Apply the default style to the entire worksheet
for row in worksheet.iter_rows():
    for cell in row:
        cell.style = default_style

# Save the workbook
excel_writer.save()
