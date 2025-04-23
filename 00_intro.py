from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

with DAG(
    dag_id='00_intro', # 이름
    description='first DAG', # 설명
    start_date=datetime(2025, 1, 1), # 시작 날짜
    catchup=False, # 이어서 작업할지
    schedule=timedelta(minutes=1), # 작업 주기(1분마다)
    # schedule='* * * * *',
) as dag:
    
    t1 = BashOperator( # task 정의
        task_id='first_task',
        bash_command='date'
    ) 

    t2 = BashOperator(
        task_id='second_task',
        bash_command='echo hello'
    )

    t1 >> t2 # task 연결