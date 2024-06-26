import csv

def read_csv_with_custom_delimiter(file_path, delimiter='^', expected_columns=54, special_columns=[]):
    reconstructed_rows = []

    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=delimiter)
        
        for row in reader:
            if len(row) != expected_columns:
                # Initialize adjusted_row and track index
                adjusted_row = []
                col_index = 0
                
                while col_index < len(row):
                    if col_index in special_columns and col_index < expected_columns:
                        # Combine columns until the expected column length is reached
                        combined_col = row[col_index]
                        while (col_index + 1 < len(row) and len(adjusted_row) < expected_columns - 1 and 
                               (len(adjusted_row) not in special_columns)):
                            col_index += 1
                            combined_col += delimiter + row[col_index]
                        adjusted_row.append(combined_col)
                    else:
                        adjusted_row.append(row[col_index])
                    col_index += 1

                # Ensure the adjusted_row has exactly the expected number of columns
                if len(adjusted_row) < expected_columns:
                    adjusted_row.extend([''] * (expected_columns - len(adjusted_row)))
                elif len(adjusted_row) > expected_columns:
                    adjusted_row = adjusted_row[:expected_columns]

                reconstructed_rows.append(adjusted_row)
            else:
                reconstructed_rows.append(row)

    return reconstructed_rows

# Example usage
file_path = 'your_file.csv'
# Assuming you know the indices of the special columns, e.g., [2, 5, 8, 12, 20, 25, 40, 50]
special_columns = [2, 5, 8, 12, 20, 25, 40, 50]
rows = read_csv_with_custom_delimiter(file_path, special_columns=special_columns)

# You can process the rows as needed, for example, printing them:
for row in rows:
    print(row)
