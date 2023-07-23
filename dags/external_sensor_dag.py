import pendulum
from airflow.decorators import dag
from airflow.sensors.external_task import ExternalTaskSensor


@dag(
    schedule="30 4 * * *",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["educative"]
)
def educative_dag8():

    ExternalTaskSensor(
        task_id="external_sensor",
        external_dag_id="educative_dag3",
        external_task_id="python_operator",
        allowed_states=["success"],
        failed_states=["failed", "skipped"],
    )

educative_dag8()