import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Float, DateTime, Text
from sqlalchemy.dialects.oracle import BLOB, CLOB, NUMBER, VARCHAR2, CHAR, DATE, TIMESTAMP

# Sample DataFrame
data = {
    'ID': [1, 2, 3],
    'NAME': ['Alice', 'Bob', 'Charlie'],
    'AGE': [25, 30, 35],
    'JOIN_DATE': [pd.Timestamp('2020-01-01'), pd.Timestamp('2021-01-01'), pd.Timestamp('2022-01-01')]
}
df = pd.DataFrame(data)

# Map Pandas dtypes to SQLAlchemy/Oracle data types
dtype_map = {
    'object': VARCHAR2(255),
    'int64': NUMBER,
    'float64': Float,
    'datetime64[ns]': DATE,
    'bool': CHAR(1),
    'bytes': BLOB
}

# Define table creation function
def generate_create_table_query(df, table_name):
    metadata = MetaData()
    columns = []

    for column_name, dtype in df.dtypes.items():
        sql_dtype = dtype_map[str(dtype)]
        columns.append(Column(column_name, sql_dtype))

    table = Table(table_name, metadata, *columns)
    create_query = str(table.compile(dialect=oracle.dialect()))
    return create_query

# Define data insertion function
def generate_insert_query(df, table_name):
    insert_queries = []
    for index, row in df.iterrows():
        values = ', '.join([repr(x) if isinstance(x, str) else str(x) for x in row])
        query = f"INSERT INTO {table_name} VALUES ({values});"
        insert_queries.append(query)
    return insert_queries

# Generate SQL queries
table_name = "MY_TABLE"
create_table_query = generate_create_table_query(df, table_name)
insert_queries = generate_insert_query(df, table_name)

# Print the generated queries
print("Create Table Query:")
print(create_table_query)
print("\nInsert Queries:")
for query in insert_queries:
    print(query)

# Connect to Oracle and execute queries (you need to set up your Oracle connection string)
engine = create_engine('oracle+cx_oracle://user:password@host:port/service_name')
connection = engine.connect()

# Execute create table query
connection.execute(create_table_query)

# Execute insert queries
for query in insert_queries:
    connection.execute(query)

connection.close()
