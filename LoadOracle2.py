import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle

# Sample DataFrame
data = {
    'ID': [1, 2, 3],
    'NAME': ['Alice', 'Bob', 'Charlie'],
    'AGE': [25, 30, 35],
    'JOIN_DATE': [pd.Timestamp('2020-01-01'), pd.Timestamp('2021-01-01'), pd.Timestamp('2022-01-01')]
}
df = pd.DataFrame(data)

# Map Pandas dtypes to Oracle data types
dtype_map = {
    'object': 'VARCHAR2(255)',
    'int64': 'NUMBER',
    'float64': 'NUMBER',
    'datetime64[ns]': 'DATE',
    'bool': 'CHAR(1)',
    'bytes': 'BLOB'
}

# Define function to generate CREATE TABLE query
def generate_create_table_query(df, table_name):
    columns = []
    for column_name, dtype in df.dtypes.items():
        sql_dtype = dtype_map[str(dtype)]
        columns.append(f"{column_name} {sql_dtype}")
    columns_str = ", ".join(columns)
    create_query = f"CREATE TABLE {table_name} ({columns_str})"
    return create_query

# Define function to generate INSERT queries
def generate_insert_queries(df, table_name):
    insert_queries = []
    for index, row in df.iterrows():
        columns = ', '.join(df.columns)
        values = ', '.join([f"'{x}'" if isinstance(x, str) else f"TO_DATE('{x}', 'YYYY-MM-DD')" if isinstance(x, pd.Timestamp) else str(x) for x in row])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        insert_queries.append(query)
    return insert_queries

# Generate SQL queries
table_name = "MY_TABLE"
create_table_query = generate_create_table_query(df, table_name)
insert_queries = generate_insert_queries(df, table_name)

# Print the generated queries
print("Create Table Query:")
print(create_table_query)
print("\nInsert Queries:")
for query in insert_queries:
    print(query)

# Connect to Oracle and execute queries
oracle_connection_string = 'oracle+cx_oracle://user:password@host:port/service_name'
engine = create_engine(oracle_connection_string)
connection = engine.connect()

# Execute create table query
connection.execute(create_table_query)

# Execute insert queries
for query in insert_queries:
    connection.execute(query)

connection.close()
