"""
Twitter DAG

This DAG (Directed Acyclic Graph) orchestrates the extraction, transformation, and loading (ETL) process
for Twitter data. It runs the Twitter ETL code defined in the `twitter_etl.py` module.

Tasks:
    - complete_twitter_etl: Executes the `run_twitter_etl` function from the `twitter_etl` module.

Default Arguments:
    - owner: The owner of the DAG.
    - depends_on_past: Specifies if a task should depend on the success of its previous run.
    - start_date: The start date of the DAG.
    - email: The email address to send email notifications to.
    - email_on_failure: Specifies whether to send an email on task failure.
    - email_on_retry: Specifies whether to send an email on task retry.
    - retries: The number of retries that should be attempted before failing the task.
    - retry_delay: The delay between retries.

Attributes:
    - dag: The DAG object representing the Twitter ETL pipeline.
"""

from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.date import days_ago
from datetime import datetime
from twitter_etl import run_twitter_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='My Twitter ETL Code'
)

run_etl = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=run_twitter_etl,
    dag=dag,
)
