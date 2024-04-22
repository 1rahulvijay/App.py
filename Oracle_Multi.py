import os
import pandas as pd
import cx_Oracle

# Database connection details
db_user = 'your_username'
db_password = 'your_password'
db_host = 'your_host'
db_port = 'your_port'
db_service_name = 'your_service_name'

# Establishing a connection to the Oracle database
connection = cx_Oracle.connect(user=db_user, password=db_password,
                               dsn=f"{db_host}:{db_port}/{db_service_name}")

# Function to load data from a file into the database
def load_data_to_db(file_path, table_name):
    # Check if table already exists
    cursor = connection.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM user_tables WHERE table_name = '{table_name.upper()}'")
    table_exists = cursor.fetchone()[0]
    cursor.close()

    # Reading data from file
    df = pd.read_csv(file_path)  # Modify this depending on your file type

    # If table exists, append data
    if table_exists:
        df.to_sql(table_name, connection, if_exists='append', index=False)
    else:
        df.to_sql(table_name, connection, if_exists='fail', index=False)

# Directory where your files are stored
files_directory = '/path/to/your/files'

# Iterate over files in the directory
for filename in os.listdir(files_directory):
    if filename.endswith('.csv'):  # Change file type if needed
        table_name = os.path.splitext(filename)[0]
        file_path = os.path.join(files_directory, filename)
        load_data_to_db(file_path, table_name)

# Commit changes and close connection
connection.commit()
connection.close()
