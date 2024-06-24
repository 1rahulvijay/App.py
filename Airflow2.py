from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from my_task import MyTask

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1, 12, 0),  # Start date in the past at 12:00 PM
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'my_task_dag',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval='0 12 * * *',  # Cron expression for 12:00 PM CEST every day
    catchup=False,  # If you don't want to backfill
)

# Define the task function
def run_my_task():
    task = MyTask()
    task.run()

# Create the PythonOperator
run_my_task_operator = PythonOperator(
    task_id='run_my_task',
    python_callable=run_my_task,
    dag=dag,
)

# Define task dependencies (if any)
# For example, if you have multiple tasks you can set dependencies like this:
# task1 >> task2

# In this case, we only have one task
run_my_task_operator
