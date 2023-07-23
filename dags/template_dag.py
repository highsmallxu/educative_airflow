import json
import os
import pendulum
from airflow.decorators import dag, task
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator



@dag(
    schedule="30 4 * * *",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["educative"],
    template_searchpath=["/usercode/sql"])
def educative_dag6():

    @task
    def setup() -> None:
        gcp_auth_key = <<gcp_auth>>

        with open('auth.json', 'w') as outfile:
            json.dump(gcp_auth_key, outfile)

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "auth.json"
        return json.load(open("auth.json","rb"))["quota_project_id"]

    auth = setup()
    bq_job = BigQueryInsertJobOperator(
        task_id="insert_query_job",
        project_id=f'{auth}',
        configuration={
            "query": {
                "query": "{% include 'sample.sql' %}",
                "useLegacySql": False,
            }
        }
    )

    auth >> bq_job

educative_dag6()