import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': ['4', '5', '6'],
    'C': [7.0, 8.0, 9.0]
}
df = pd.DataFrame(data)

# Custom function to format data types based on column names
def format_data_type(value, column_name):
    if 'int' in column_name:
        return int(value)
    elif 'float' in column_name:
        return float(value)
    else:
        return str(value)

# Apply the custom function to all columns
formatted_df = df.applymap(lambda x: format_data_type(x, df.columns[df.columns.get_loc(x)]))

print(formatted_df)
