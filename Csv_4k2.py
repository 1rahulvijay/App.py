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
        reader = csv.reader(f)
        headers = next(reader)  # Read the header row
        
        # Determine the index to split
        index_to_split = 50
        
        # Adjust headers to include new columns next to the original column
        new_headers = headers[:index_to_split + 1] + ["col2", "col3", "col4"] + headers[index_to_split + 1:]
        
        rows = []

        for row in reader:
            original_string = row[index_to_split]
            split_data = split_string(original_string)
            
            # Construct new row with the split parts inserted next to the original column
            new_row = row[:index_to_split] + [split_data[0]] + [split_data[1], split_data[2], split_data[3]] + row[index_to_split + 1:]
            rows.append(new_row)

    # Write the updated rows to a new CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(new_headers)
        writer.writerows(rows)

# Example usage:
input_file = open('input.csv', 'rb')  # Provide the correct path to your input CSV file
output_file = 'output.csv'  # Provide the correct path to your output CSV file
process_csv(input_file, output_file)
input_file.close()
