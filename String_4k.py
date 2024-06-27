def split_string_into_columns(data, column_index, max_length=4000, num_columns=4):
    for row in data:
        # Split the long string at the specified column index
        long_string = row[column_index]
        # Create a list of chunks of the long string
        chunks = [long_string[i:i+max_length] for i in range(0, len(long_string), max_length)]
        
        # Ensure the list of chunks has exactly `num_columns` elements
        while len(chunks) < num_columns:
            chunks.append('')

        # Replace the original long string in the row with the first chunk
        row[column_index] = chunks[0]
        # Add the rest of the chunks as new columns in the row
        row.extend(chunks[1:num_columns])
    
    return data

# Example usage
data = [
    ["value1", "value2", "short_string", "value4", "very_long_string_that_needs_splitting" * 2400, "value6"],
    # ... (other rows)
]

split_data = split_string_into_columns(data, column_index=4, max_length=4000, num_columns=4)

for row in split_data:
    print(row)
