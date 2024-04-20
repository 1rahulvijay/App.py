import pandas as pd
import re

# Example DataFrame with column names containing white spaces, numerical values, and random characters
df = pd.DataFrame({' A 1@': [1, 2, 3], 'B2!': [4, 5, 6], 'C 3': [7, 8, 9]})

# Remove white spaces, numerical values, and random characters from column names
df.rename(columns=lambda x: re.sub(r'[^a-zA-Z]', '', x), inplace=True)

# Now the DataFrame will have cleaned column names
print(df)