import pandas as pd
import re

# Sample DataFrame
data = {'text': ['This is a sample text with special characters!@#',
                 'Another example text with special characters%^&']}

df = pd.DataFrame(data)

# Selecting first 255 characters and removing special characters
df['text'] = df['text'].str[:255].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))

print(df)
