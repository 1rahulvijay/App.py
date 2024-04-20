import cx_Oracle
from datetime import datetime, timedelta


def connect_to_database():
    # Update the connection string with your Oracle database credentials
    connection = cx_Oracle.connect("username", "password", "hostname:port/service_name")
    return connection


def fetch_data_from_database(date):
    connection = connect_to_database()
    cursor = connection.cursor()

    # Assuming 'your_table' is the name of the table storing your data
    # Adjust the query according to your table structure
    query = (
        f"SELECT * FROM your_table WHERE date_column = TO_DATE('{date}', 'YYYY-MM-DD')"
    )

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    connection.close()

    return data


def get_business_day_before(date):
    # Assuming date is in 'YYYY-MM-DD' format
    date = datetime.strptime(date, "%Y-%m-%d")

    # Keep subtracting 1 day until we find a business day (Monday to Friday)
    while date.weekday() > 4:
        date -= timedelta(days=1)

    return date.strftime("%Y-%m-%d")


def compare_data(past_date):
    # Fetch data for the past date
    past_data = fetch_data_from_database(past_date)

    # Get the business day before the past date
    previous_business_day = get_business_day_before(past_date)

    # Fetch data for the previous business day
    previous_data = fetch_data_from_database(previous_business_day)

    # Compare data and return only new data
    new_data = [data for data in past_data if data not in previous_data]

    return new_data


if __name__ == "__main__":
    # Specify the past date for which you want to compare the data
    past_date = "2024-04-19"

    new_data = compare_data(past_date)

    if new_data:
        print("New data found for", past_date)
        for row in new_data:
            print(row)
    else:
        print("No new data found for", past_date)
