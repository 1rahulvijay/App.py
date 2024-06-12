import csv

def read_csv_with_custom_delimiter(file_path, delimiter='^', expected_columns=54, special_column=41):
    reconstructed_rows = []

    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=delimiter)
        
        for row in reader:
            if len(row) != expected_columns:
                adjusted_row = row[:expected_columns]  # Start with the original row content
                if special_column < len(row):
                    combined_col = row[special_column]
                    for i in range(special_column + 1, len(row)):
                        combined_col += delimiter + row[i]
                    adjusted_row[special_column] = combined_col
                else:
                    adjusted_row += [''] * (expected_columns - len(adjusted_row))
                reconstructed_rows.append(adjusted_row)
            else:
                reconstructed_rows.append(row)

    return reconstructed_rows

# Example usage
file_path = 'your_file.csv'
# Assuming column 41 is the special column containing the delimiter '^'
rows = read_csv_with_custom_delimiter(file_path, special_column=41)

# Process the rows as needed, for example, printing them:
for row in rows:
    print(row) 
