import cx_Oracle
import pandas as pd

# Connect to Oracle database
connection = cx_Oracle.connect("username", "password", "hostname:port/service_name")

# Create a cursor
cursor = connection.cursor()

# Create a table in Oracle if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS your_table_name (
    column1 datatype,
    column2 datatype,
    ...
)
"""
cursor.execute(create_table_query)

# Define your DataFrame with the data you want to load
data = pd.DataFrame({
    'column1': [value1, value2, ...],
    'column2': [value1, value2, ...],
    ...
})

# Identify a unique identifier column in your data
unique_identifier_column = "unique_id_column"

# Iterate over the DataFrame and insert data into Oracle incrementally
for index, row in data.iterrows():
    # Check if the unique identifier already exists in the database
    check_query = f"SELECT COUNT(*) FROM your_table_name WHERE {unique_identifier_column} = :1"
    cursor.execute(check_query, (row[unique_identifier_column],))
    result = cursor.fetchone()

    # If the data doesn't exist, insert it into the database
    if result[0] == 0:
        insert_query = """
        INSERT INTO your_table_name (column1, column2, ...)
        VALUES (:1, :2, ...)
        """
        cursor.execute(insert_query, tuple(row))

# Commit the changes
connection.commit()

# Close cursor and connection
cursor.close()
connection.close()
