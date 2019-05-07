import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

def save_world(**kwargs):
    return 'world'

def print_xcom(**kwargs):
    ti = kwargs['ti']
    string = ti.xcom_pull(task_ids='save_world')
    print(string)

default_args = {
    'owner': 'Tiritilli',
    'start_date': dt.datetime(2019, 6, 1),
    'retries': 2,
    'retry_delay': dt.timedelta(minutes=3),
    'provide_context': True
}

with DAG('Sleep',
         default_args=default_args,
         schedule_interval='@once',
         ) as dag:

    opr_print_hello = BashOperator(
        task_id='print_hello',
        bash_command='echo "hello"'
    )

    opr_sleep = BashOperator(
        task_id='sleep',
        bash_command='sleep 5'
    )

    opr_save_world = PythonOperator(
        task_id='save_world',
        python_callable=save_world
    )

    opr_print_xcom = PythonOperator(
        task_id='print_xcom',
        python_callable=print_xcom
    )

opr_print_hello >> opr_sleep >> opr_save_world >> opr_print_xcom