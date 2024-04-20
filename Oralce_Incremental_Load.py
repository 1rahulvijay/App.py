import cx_Oracle
from datetime import datetime, timedelta
import pandas as pd
import logging

# Set up logging
logging.basicConfig(
    filename="oracle_data_loader.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


# Function to establish a connection to the Oracle database
def connect_to_oracle(username, password, host, port, service_name):
    try:
        connection = cx_Oracle.connect(
            user=username,
            password=password,
            dsn=cx_Oracle.makedsn(host, port, service_name=service_name),
        )
        logging.info("Connected to Oracle database successfully")
        return connection
    except cx_Oracle.DatabaseError as e:
        logging.error("Failed to connect to Oracle database: %s", str(e))
        raise


# Function to load data into Oracle
def load_data(connection, data):
    try:
        cursor = connection.cursor()
        # Assuming 'data' is a DataFrame with columns matching the database table
        for index, row in data.iterrows():
            cursor.execute(
                "INSERT INTO your_table_name VALUES (:1, :2, :3, ...)", row.tolist()
            )
        cursor.close()
        connection.commit()
        logging.info("Data loaded into Oracle successfully")
    except cx_Oracle.DatabaseError as e:
        logging.error("Failed to load data into Oracle: %s", str(e))
        connection.rollback()
        raise


# Function to delete data older than the last 3 business days
def delete_old_data(connection):
    try:
        cursor = connection.cursor()
        # Calculate the date 3 business days ago
        today = datetime.now()
        three_days_ago = today - timedelta(days=3)
        # You may need to adjust this query depending on your database schema
        query = "DELETE FROM your_table_name WHERE your_date_column < TO_DATE(:1, 'YYYY-MM-DD')"
        cursor.execute(query, (three_days_ago.strftime("%Y-%m-%d"),))
        cursor.close()
        connection.commit()
        logging.info("Old data deleted from Oracle successfully")
    except cx_Oracle.DatabaseError as e:
        logging.error("Failed to delete old data from Oracle: %s", str(e))
        connection.rollback()
        raise


# Example function to load incremental data (replace this with your actual data loading logic)
def load_incremental_data():
    # Example of loading data from a CSV file
    try:
        data = pd.read_csv("your_incremental_data.csv")
        return data
    except Exception as e:
        logging.error("Failed to load incremental data: %s", str(e))
        raise


# Example usage
if __name__ == "__main__":
    try:
        # Database connection details
        username = "your_username"
        password = "your_password"
        host = "your_host"
        port = "your_port"
        service_name = "your_service_name"

        # Connect to Oracle
        connection = connect_to_oracle(username, password, host, port, service_name)

        # Load your incremental data
        incremental_data = load_incremental_data()

        # Load data into Oracle
        load_data(connection, incremental_data)

        # Delete old data
        delete_old_data(connection)

        # Close connection
        connection.close()
    except Exception as e:

        logging.error("An error occurred: %s", str(e))
