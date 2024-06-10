import csv

def read_csv_with_custom_delimiter(file_path, delimiter='^', expected_columns=54, special_columns=[]):
    reconstructed_rows = []

    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=delimiter)
        for row in reader:
            if len(row) != expected_columns:
                # Handle special columns
                adjusted_row = []
                col_index = 0
                
                for col in row:
                    if col_index in special_columns:
                        # Join back the split columns for special columns
                        adjusted_col = [col]
                        while col_index + 1 < len(row) and col_index + 1 in special_columns:
                            col_index += 1
                            adjusted_col.append(row[col_index])
                        adjusted_row.append(delimiter.join(adjusted_col))
                    else:
                        adjusted_row.append(col)
                    
                    col_index += 1
                
                # Add remaining columns if any
                if col_index < len(row):
                    adjusted_row.extend(row[col_index:])
                
                # Ensure the row has the correct number of columns
                while len(adjusted_row) < expected_columns:
                    adjusted_row.append('')
                
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
