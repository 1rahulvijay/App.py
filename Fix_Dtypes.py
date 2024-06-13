from datetime import datetime

# Define conversion functions
def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None  # or handle it as you prefer

def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None  # or handle it as you prefer

def convert_to_string(value):
    return str(value)

def convert_to_date(value, date_format='%Y-%m-%d'):
    try:
        return datetime.strptime(value, date_format)
    except ValueError:
        return None  # or handle it as you prefer

# General conversion function
def convert_value(value, desired_type, date_format='%Y-%m-%d'):
    if desired_type == 'int':
        return convert_to_int(value)
    elif desired_type == 'float':
        return convert_to_float(value)
    elif desired_type == 'string':
        return convert_to_string(value)
    elif desired_type == 'date':
        return convert_to_date(value, date_format)
    else:
        return value

# Function to iterate over the list and convert data types
def convert_list(data, column_types, date_format='%Y-%m-%d'):
    converted_data = [
        [convert_value(item, column_types[i], date_format) for i, item in enumerate(row)]
        for row in data
    ]
    return converted_data

# Example usage
data = [
    ['1', '2.5', 'hello', '2023-01-01'],
    ['2', '3.6', 'world', '2023-01-02'],
    # ... more rows
]

column_types = ['int', 'float', 'string', 'date']  # Define the desired type for each column

converted_data = convert_list(data, column_types)

# Optionally, print the first few rows to verify
print(converted_data[:5])
