import pandas as pd
import re

# Sample DataFrame
data = {'text': ['This is    a sample    text    with   multiple     white spaces',
                 'Another   example   text   with    extra     spaces    ']}

df = pd.DataFrame(data)

# Removing multiple white spaces
df['text'] = df['text'].str.replace(r'\s+', ' ')

print(df)
