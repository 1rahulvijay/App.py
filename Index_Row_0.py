import pandas as pd

# Assuming df is your DataFrame

# Filter columns starting with 'Unnamed'
unnamed_columns = df.filter(regex=r'^Unnamed')

# Get the values of the first row to use as new column names
new_column_names = df.iloc[0]

# Rename the columns with the values from the first row
unnamed_columns.columns = new_column_names

# Update the original DataFrame with the renamed columns
df.update(unnamed_columns)

# Drop the first row (since it's now the column names)
df = df.drop(0)

# Now df has columns starting with 'Unnamed' renamed with values from the first row
