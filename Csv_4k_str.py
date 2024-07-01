import csv
import io

def split_string(s):
    col1 = s[:4000]
    col2 = s[4000:8000] if len(s) > 4000 else ""
    col3 = s[8000:12000] if len(s) > 8000 else ""
    col4 = s[12000:16000] if len(s) > 12000 else ""
    return [col1, col2, col3, col4]

def process_csv(input_file, output_file):
    with io.TextIOWrapper(input_file, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ["col1", "col2", "col3", "col4"]
        rows = []

        for row in reader:
            original_string = row[fieldnames[50]]
            split_data = split_string(original_string)
            
            # Update the row with new columns
            row["col1"], row["col2"], row["col3"], row["col4"] = split_data
            
            # Append the updated row to the list
            rows.append(row)

    # Write the updated rows to a new CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

# Example usage:
input_file = open('input.csv', 'rb')  # Provide the correct path to your input CSV file
output_file = 'output.csv'  # Provide the correct path to your output CSV file
process_csv(input_file, output_file)
input_file.close()
