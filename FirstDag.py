#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 14:29:21 2020

@author: jonathanbrooks
"""

from airflow import DAG
from airflow.operators import BashOperator,PythonOperator
from datetime import datetime, timedelta


default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'email': ['airflow@airflow.com'],
        'email_on_failure': False,
        'start_date': datetime(2020,6,6),
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
      }

dag = DAG('simple', schedule_interval='*/5 * * * *', default_args=default_args)

t1 = BashOperator(
    task_id='testairflow',
    bash_command='python /users/jonathanbrooks/airflow/dags/airflowtest.py',
    dag=dag)
