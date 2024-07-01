import csv
import io
from datetime import datetime

def split_string(s):
    col1 = s[:4000]
    col2 = s[4000:8000] if len(s) > 4000 else ""
    col3 = s[8000:12000] if len(s) > 8000 else ""
    col4 = s[12000:16000] if len(s) > 12000 else ""
    return [col1, col2, col3, col4]

def format_header(header):
    return [h.strip() for h in header]

def format_values(row, new_header):
    return tuple(row[h] for h in new_header)

BATCH_SIZE = 1000
index_to_split = 49  # 50th column in a 0-indexed list

with conn.cursor() as cursor:
    with open(csv_file_path, 'rb') as file:
        reader = csv.reader(io.TextIOWrapper(file, encoding='utf-8', newline=''), delimiter=',')
        original_header = format_header(next(reader))
        
    with open(csv_file_path, 'rb') as file:
        reader = csv.DictReader(io.TextIOWrapper(file, encoding='utf-8', newline=''), delimiter=',', fieldnames=original_header)
        next(reader)  # Skip the header row
        
        # Insert new columns into header
        new_header = original_header[:index_to_split + 1] + ["col2", "col3", "col4"] + original_header[index_to_split + 1:]

        # Format query with new header
        query = f"INSERT INTO ICM.CRMS_DOCS_WITH_FACS_NEW ({', '.join(new_header)}) VALUES ({', '.join([':' + str(x) for x in range(1, len(new_header) + 1)])})"
        cursor.setinputsizes(*[str for _ in new_header])  # Assuming all columns are strings, adjust as necessary
        
        data = []
        for row in reader:
            original_string = row[original_header[index_to_split]]
            split_data = split_string(original_string)
            
            # Create new row with split data
            new_row = row.copy()
            new_row[original_header[index_to_split]] = split_data[0]
            new_row["col2"] = split_data[1]
            new_row["col3"] = split_data[2]
            new_row["col4"] = split_data[3]
            
            data.append(format_values(new_row, new_header))
            
            if len(data) % BATCH_SIZE == 0:
                cursor.executemany(query, data)
                data = []

        if data:
            cursor.executemany(query, data)
        
    conn.commit()
end = datetime.now()
print(f"Process completed at {end}")
