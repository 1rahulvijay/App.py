from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import pytz
from my_class import MyClass

# Function to generate runtime parameters and execute the class method
def execute_class_method(**kwargs):
    # Generate runtime parameters
    param1 = "runtime_param1"
    param2 = "runtime_param2"

    # Instantiate the class with the parameters
    my_instance = MyClass(param1, param2)

    # Execute the method
    my_instance.my_method()

# Define the default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),  # Set the start date to one day ago
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the timezone
ce_tz = pytz.timezone('Europe/Berlin')

# Define the DAG
dag = DAG(
    'my_daily_python_class_method',
    default_args=default_args,
    description='A DAG to execute a class method with runtime parameters',
    schedule_interval='0 12 * * *',  # Every day at 12:00 PM
    start_date=datetime(2023, 1, 1, tzinfo=ce_tz),  # Set the timezone for start_date
    catchup=False,  # Do not perform a catchup
)

# Define the task
run_class_method = PythonOperator(
    task_id='run_class_method',
    python_callable=execute_class_method,
    provide_context=True,  # To pass context to the function
    dag=dag,
)

# Set the task dependencies
run_class_method
