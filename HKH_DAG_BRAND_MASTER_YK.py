from hkh.src.HKH_DIAPER_CLASSIFY_BRAND_NAME_YK import classify_diaper_brand_name

from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner' : 'HKH',
    'depends_on_past' : False,
    'start_date':datetime(2019,9,10),
    'retries':3,
    'retry_delay':timedelta(hours = 1)
}

dag = DAG('HKH_BRAND_MASTER_YK',
         default_args=default_args,
         dagrun_timeout=timedelta(days=1),
         description="HKH_BRAND_MASTER_YK",
         schedule_interval='0 23 * * *')

classify_diaper_brand_name_op = PythonOperator(
        task_id='yk_brand_classfiy_processing',
        python_callable=classify_diaper_brand_name,
        dag=dag)
