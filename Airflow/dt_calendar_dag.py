import psycopg2 as pg 
import logging
import csv
import pandas as pd
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator 


default_args = {
	'owner': 'dtemlyukov',
	'depends_on_past': False,
	'start_date': datetime(2019,12,12),
	'retries': 0,
	'retry_delay': timedelta(minutes = 5),
	'provide_context': True,
}

DAG_NAME = 'dt_calendar_dag'

dag = DAG(DAG_NAME,
			description = 'Test job for calendar',
			schedule_interval = '@once',
			default_args=default_args,
			catchup = False,
			max_active_runs = 1)

param = """
		full_date date,
		weekens int,
		day_before_weekends int,
		rescheduled int
		"""


def drop_table(**kwargs):
	conn = pg.connect(host = "localhost", database = "postgres", user = kwargs.get('user'), password = kwargs.get('password'))
	cursor = conn.cursor()
	logging.info('create connection')
	table_schema = kwargs.get('table_schema', None)
	table_name = kwargs.get('table_name', None)
	full_name = ''
	if table_schema:
		full_name = table_schema + '.' + full_name
	full_name += table_name
	drop_statement = 'drop table if exists {}'.format(full_name)
	cursor.execute(drop_statement)
	conn.commit()
	logging.info('table {} dropped'.format(full_name))
	conn.close()

def create_table(**kwargs):
	conn = pg.connect(host = "localhost", database = "postgres", user = kwargs.get('user'), password = kwargs.get('password'))
	cursor = conn.cursor()
	logging.info('create connection')
	table_schema = kwargs.get('table_schema', None)
	table_name = kwargs.get('table_name', None)
	param = kwargs.get('param','')
	full_name = ''
	if table_schema:
		full_name = table_schema + '.' + full_name
	full_name += table_name
	create_statement = 'create table if not exists {}({})'.format(full_name, param)
	cursor.execute(create_statement)
	conn.commit()
	logging.info(f'table {full_name} created')
	conn.close()

def insert_values(**kwargs):
	conn = pg.connect(host = "localhost", database = "postgres", user = kwargs.get('user'), password = kwargs.get('password'))
	cursor = conn.cursor()
	logging.info('create connection')
	table_schema = kwargs.get('table_schema', None)
	table_name = kwargs.get('table_name', None)
	full_name = ''
	if table_schema:
		full_name = table_schema + '.' + full_name
	full_name += table_name

	weekends=[]
	day_before_weekends=[]
	rescheduled=[]
	datelist = pd.date_range('1999-1-1','2025-12-31')
	datelist = pd.DataFrame([i.strftime('%Y-%m-%d') for i in datelist])
	datelist ['weekends'] = 0
	datelist ['day_before_weekends'] = 0
	datelist ['rescheduled'] = 0
	with open('/usr/data/calendar-20191112T1247.csv', 'rt') as f:
		data = pd.read_csv(f)
		for row in range(len(data)):
			for col in range(1,13):
				for element in (str(data.iloc[row][col]).split(',')):
					if '*' in element:
						day_before_weekends.append(str(data.iloc[row][0]) + '-' + str(col) + '-' + element.split('*')[0])
					elif '+' in element:
						rescheduled.append(str(data.iloc[row][0]) + '-' + str(col) + '-' + element.split('+')[0])
					else:
						weekends.append(str(data.iloc[row][0]) + '-' + str(col) + '-' + element)

	insert_list = []
	day_before_weekends = [str(datetime.strptime(i,'%Y-%m-%d').date()) for i in day_before_weekends]
	rescheduled = [str(datetime.strptime(i,'%Y-%m-%d').date()) for i in rescheduled]
	weekends = [str(datetime.strptime(i,'%Y-%m-%d').date()) for i in weekends]
	for i in range(len(datelist)):
		if datelist.iloc[i][0] in weekends:
			datelist.loc[i,'weekends'] = 1
		if datelist.iloc[i][0] in day_before_weekends:
			datelist.loc[i,'day_before_weekends'] = 1
		if datelist.iloc[i][0] in rescheduled:
			datelist.loc[i,'rescheduled'] = 1
		insert_list.append("('{}', {}, {}, {})".format(datelist.iloc[i][0], datelist.loc[i,'weekends'], datelist.loc[i,'day_before_weekends'], datelist.loc[i,'rescheduled']))


	create_statement = 'insert into {} values {}'.format(full_name, ',\n'.join(insert_list))
	cursor.execute(create_statement)
	conn.commit()
	logging.info(f'Data inserted in {full_name}')
	conn.close()



drop_calendar_task = PythonOperator(
	task_id = 'drop_calendar_table',
	python_callable = drop_table,
	op_kwargs = { 'user': 'student',
					'password': 'study',
					'table_schema': 'public',
					'table_name': 'dt_calendar'
					},
				dag = dag

)

create_calendar_task = PythonOperator(
	task_id = 'create_calendar_table',
	python_callable = create_table,
	op_kwargs = { 'user': 'student',
					'password': 'study',
					'table_schema': 'public',
					'table_name': 'dt_calendar',
					'param': param
					},
				dag = dag

)

insert_values_task = PythonOperator(
	task_id = 'insert_values_task',
	python_callable = insert_values,
	op_kwargs = { 'user': 'student',
					'password': 'study',
					'table_schema': 'public',
					'table_name': 'dt_calendar',
					},
				dag = dag

)



drop_calendar_task >> create_calendar_task >> insert_values_task
