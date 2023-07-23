import pendulum
from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from airflow.datasets import Dataset

dag1_dataset = Dataset("s3://dag1/output_1.txt", extra={"hi": "bye"})

@dag(
    schedule="30 4 * * *",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["educative"]
)
def educative_dag9_producer():
    BashOperator(outlets=[dag1_dataset], task_id="producer", bash_command="sleep 5")

educative_dag9_producer()

@dag(
    schedule=[dag1_dataset],
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["educative"]
)
def educative_dag9_consumer():
    BashOperator(task_id="consumer", bash_command="sleep 5")

educative_dag9_consumer()