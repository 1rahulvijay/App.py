def split_string_into_columns(data, column_index, max_length=4000, num_columns=4):
    for row in data:
        # Get the long string from the specified column
        long_string = row[column_index]
        
        # Split the long string into chunks of max_length
        chunks = [long_string[i:i + max_length] for i in range(0, len(long_string), max_length)]
        
        # Ensure we have exactly num_columns chunks by adding empty strings if needed
        while len(chunks) < num_columns:
            chunks.append('')
        
        # Update the row with the chunks, ensuring we have exactly num_columns
        for i in range(num_columns):
            if column_index + i < len(row):
                row[column_index + i] = chunks[i]
            else:
                row.append(chunks[i])
        
        # Ensure the row has exactly num_columns after the column_index
        while len(row) < column_index + num_columns:
            row.append('')
    
    return data

# Example usage
data = [
    ["value1", "value2", "short_string", "value4", "very_long_string_that_needs_splitting" * 3, "value6"],
    ["value1", "value2", "short_string", "value4", "short_string", "value6"],
    ["value1", "value2", "short_string", "value4", "another_very_long_string_that_needs_splitting" * 5, "value6"]
]

split_data = split_string_into_columns(data, column_index=4, max_length=4000, num_columns=4)

for row in split_data:
    print(row)
