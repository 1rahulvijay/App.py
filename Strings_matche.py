import re
import pandas as pd

mylist = ['dog', 'cat', 'fish']
pattern = '|'.join(mylist)

def pattern_searcher(search_str: str, search_list: str):
    search_obj = re.findall(search_list, search_str)
    if search_obj:
        return search_obj
    else:
        return ['NA']

# Sample DataFrame
data = {'a': ['I have a dog and a cat', 'A fish is in the pond', 'No pets here']}
frame = pd.DataFrame(data)

# Apply the function and expand the results into multiple columns
frame['matched_str'] = frame['a'].apply(lambda x: pattern_searcher(search_str=x, search_list=pattern))
expanded_frame = frame['matched_str'].apply(pd.Series)

# Rename columns to reflect the pattern matches
expanded_frame.columns = [f'matched_str_{i+1}' for i in range(expanded_frame.shape[1])]

# Concatenate the original frame with the expanded_frame
frame = pd.concat([frame, expanded_frame], axis=1).drop(columns=['matched_str'])

print(frame)
