import cx_Oracle
import pandas as pd


def insert_dataframe_to_oracle(df, username, password, connection_string, table_name):
    # Connect to the Oracle database
    conn = cx_Oracle.connect(username, password, connection_string)

    # Convert int64 values to int
    df = df.apply(lambda x: x.astype(int) if pd.api.types.is_integer_dtype(x) else x)

    # Insert data into Oracle table
    cursor = conn.cursor()
    for index, row in df.iterrows():
        columns = ", ".join(row.index)
        placeholders = ", ".join([":" + str(i + 1) for i in range(len(row))])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(query, tuple(row))
        conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()


# Sample data with int64 values
data = {"id": [1, 2, 3], "value": [123, 456, 789]}
df = pd.DataFrame(data)

# Database connection details
username = "your_username"
password = "your_password"
connection_string = "your_connection_string"
table_name = "your_table_name"

# Insert data into Oracle table
insert_dataframe_to_oracle(df, username, password, connection_string, table_name)
