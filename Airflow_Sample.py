from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import logging


# Define the Python function that you want to execute
def my_python_function(param1, param2, **kwargs):
    try:
        logging.info(
            "Executing my Python script with parameters: param1={}, param2={}".format(
                param1, param2
            )
        )

        # Your Python script code here
        # For demonstration, let's just print the parameters
        print("Parameter 1:", param1)
        print("Parameter 2:", param2)

        # You can access other context variables via **kwargs
        # For example, execution_date = kwargs['execution_date']

        logging.info("Execution completed successfully")
    except Exception as e:
        logging.error("An error occurred: {}".format(str(e)))
        raise e


# Define the default arguments for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 4, 19),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    "advanced_python_script_dag",
    default_args=default_args,
    description="An advanced DAG to schedule execution of a Python script",
    schedule_interval=timedelta(days=1),  # This sets the schedule to run once a day
)

# Define a list of tasks with parameters
tasks_with_parameters = [
    {"task_id": "task_1", "param1": "value1", "param2": "value2"},
    {"task_id": "task_2", "param1": "value3", "param2": "value4"},
    # Add more tasks as needed
]

# Generate tasks dynamically based on the list of tasks with parameters
for task_params in tasks_with_parameters:
    task_id = task_params["task_id"]
    param1 = task_params["param1"]
    param2 = task_params["param2"]

    execute_python_script_task = PythonOperator(
        task_id=task_id,
        python_callable=my_python_function,
        op_kwargs={"param1": param1, "param2": param2},
        provide_context=True,
        dag=dag,
    )

    # Set dependencies between tasks if needed
    # execute_python_script_task.set_upstream(...)
