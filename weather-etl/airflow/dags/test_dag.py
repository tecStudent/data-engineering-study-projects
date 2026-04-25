from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import json

def criar_arquivo_teste():
    pasta = "/opt/airflow/storage/raw"
    os.makedirs(pasta, exist_ok=True)

    caminho_arquivo = os.path.join(pasta, "teste_output.json")

    dados = {
        "status": "ok",
        "mensagem": "arquivo criado com sucesso",
        "data_execucao": str(datetime.now())
    }

    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

    print(f"Arquivo criado em: {caminho_arquivo}")

with DAG(
    dag_id="test_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["teste"],
) as dag:

    task_criar_arquivo = PythonOperator(
        task_id="criar_arquivo_teste",
        python_callable=criar_arquivo_teste
    )