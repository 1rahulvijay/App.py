import pandas as pd

def generate_create_table_query(df, table_name):
    create_query = f"CREATE TABLE {table_name} (\n"
    for column in df.columns:
        dtype = df[column].dtype
        if dtype == 'object':
            sql_type = 'VARCHAR(255)'
        elif dtype == 'int64':
            sql_type = 'INT'
        elif dtype == 'float64':
            sql_type = 'FLOAT'
        else:
            sql_type = 'VARCHAR(255)'  # default to VARCHAR
        create_query += f"    {column} {sql_type},\n"
    create_query = create_query.rstrip(',\n') + "\n);"
    return create_query

def main():
    # Example DataFrame
    data = {
        'ID': [1, 2, 3],
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]
    }
    df = pd.DataFrame(data)

    # Table name
    table_name = 'example_table'

    # Generate create table query
    create_table_query = generate_create_table_query(df, table_name)

    # Write to file
    with open('table_schema.sql', 'w') as f:
        f.write(create_table_query)

if __name__ == "__main__":
    main()
