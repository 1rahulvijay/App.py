import pandas as pd

# Step 2: Define your DataFrame
data = {
    'col1': ['apple', 'banana', 'cherry'],
    'col2': ['dog', 'elephant', 'frog'],
    'col3': ['green', 'yellow', 'red']
}
df = pd.DataFrame(data)

# Step 3: Define the list of values to search
values_to_search = ['apple', 'elephant', 'red']

# Step 4: Create a function to check for values and create new columns
def create_columns_based_on_values(row, values):
    new_cols = {}
    for value in values:
        new_cols[f'contains_{value}'] = any(value in cell for cell in row)
    return pd.Series(new_cols)

# Step 5: Apply the function to the DataFrame and create new columns
new_columns = df.apply(create_columns_based_on_values, values=values_to_search, axis=1)
df = pd.concat([df, new_columns], axis=1)

print(df)
