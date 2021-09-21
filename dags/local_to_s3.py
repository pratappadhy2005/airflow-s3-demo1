from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator, ShortCircuitOperator
from validate_policy import validateJSON
from s3_upload import pushS3
from create_manifest import edapPolicy

default_args = {
    'owner': 'Airflow',
    'start_date': datetime(2021, 2, 28),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

with DAG("S3_UPLOAD",default_args=default_args, schedule_interval="@daily", catchup=False) as dag:
    t1=ShortCircuitOperator(task_id="Validate-Policy-Files", provide_context=True, python_callable=validateJSON)
    t2=PythonOperator(task_id="Read-Policy-And-Create-Manifest-Python", provide_context=True, python_callable=edapPolicy)
    t3=PythonOperator(task_id="S3-Using-Python", provide_context=True, python_callable=pushS3)

    t1 >> t2 >> t3