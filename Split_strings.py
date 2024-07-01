def split_string(s):
    col1 = s[:4000]
    col2 = s[4000:8000] if len(s) > 4000 else ""
    col3 = s[8000:12000] if len(s) > 8000 else ""
    col4 = s[12000:16000] if len(s) > 12000 else ""
    return [col1, col2, col3, col4]

# Assuming 'strings' is your list and you want to apply the function to the element at index 50
index = 50
string_to_split = strings[index]  # Extracting the string at index 50

# Splitting the string
split_data = split_string(string_to_split)

# Updating the original list with the split parts
strings[index] = split_data[0]
strings.insert(index + 1, split_data[1])
strings.insert(index + 2, split_data[2])
strings.insert(index + 3, split_data[3])

# Printing the updated list
for i in range(index, index + 4):
    print(f"strings[{i}] = {strings[i]}")
