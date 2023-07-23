from airflow.operators.trigger_dagrun import TriggerDagRunOperator
import pendulum
from airflow.decorators import dag

@dag(
    schedule="30 4 * * *",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["educative"]
)
def educative_dag7():

    TriggerDagRunOperator(
        task_id="trigger_dagrun",
        trigger_dag_id="educative_dag1", 
        conf={},
    )

educative_dag7()