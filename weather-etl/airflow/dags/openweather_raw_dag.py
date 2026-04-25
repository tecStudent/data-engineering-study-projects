from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from src.extract.openweather import extract_current_weather, save_raw_weather


def extract_and_save():
    payload = extract_current_weather()
    output_path = save_raw_weather(payload)
    print(f"Payload salvo em: {output_path}")


with DAG(
    dag_id="openweather_raw_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["weather", "raw"],
) as dag:

    extract_and_save_task = PythonOperator(
        task_id="extract_and_save_current_weather",
        python_callable=extract_and_save,
    )