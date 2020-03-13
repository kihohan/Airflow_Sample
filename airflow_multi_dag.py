# update date: 2020-02-27.
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

from tkcho.src.jnj_tokenize import tkn_daily

from hkh.src.HKH_JNJ_BRAND_CLASSIFICATION import jnj_brand_classification
from hkh.src.HKH_JNJ_MASTERING_S_SP import s_sp_item_result

default_args = {
    'owner' : 'tkcho',
    'depends_on_past' : False,
    'start_date':datetime(2020,3,3),
    'retries':3,
    'retry_delay':timedelta(minutes=1)
}

dag = DAG('CTK_JNJ_MASTER',
         default_args = default_args,
         dagrun_timeout=timedelta(days=1),
         description="jnj mastering starting with tokenizing",
         schedule_interval='0 1 * * *')

# 0. dummy
op_starting = DummyOperator(task_id='execute', dag=dag)
# 1. tokenize
op_tokenize = PythonOperator(
            task_id=f'tkn_daily',
            python_callable=tkn_daily,
            dag=dag)
# 2. brand_classification
op_brand_classification = PythonOperator(
            task_id='jnj_brand_classification',
            python_callable=jnj_brand_classification,
            dag=dag)
# 3. mastering s_sp_item
op_s_sp_item_result = PythonOperator(
            task_id='s_sp_item_result',
            python_callable=s_sp_item_result,
            dag=dag)

op_starting.set_downstream(op_tokenize)
op_tokenize.set_downstream(op_brand_classification)
op_brand_classification.set_downstream(op_s_sp_item_result)
