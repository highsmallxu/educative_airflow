from airflow.decorators import dag, task
from airflow.sensors.time_delta import TimeDeltaSensor
from datetime import timedelta
from airflow.operators.bash import BashOperator
import logging
import pendulum

# dag3
@dag(
    schedule="30 4 * * *",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["educative"]
)
def educative_dag3():

    s1 = TimeDeltaSensor(task_id="time_sensor", delta=timedelta(seconds=2))
    o1 = BashOperator(task_id="bash_operator", bash_command="echo run a bash script")
    @task
    def python_operator() -> None:
        logging.info("run a python function")
    o2 = python_operator()

    s1 >> o1 >> o2

educative_dag3()