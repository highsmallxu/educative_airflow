#!/bin/bash

python /usercode/setup/setup.py
echo 'export GOOGLE_APPLICATION_CREDENTIALS=auth.json' >> ~/.bashrc
echo 'export AIRFLOW_CONN_FRANKFURTER_API=http://https://api.frankfurter.app/' >> ~/.bashrc
source ~/.bashrc