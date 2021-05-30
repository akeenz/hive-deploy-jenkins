import os
import pymysql
import pandas as pd
DEPLOYMENT_ENV=os.getenv('DEPLOYMENT_ENV')
DB_HOST="chalice-test.c4pa6qyxzm5o.us-east-2.rds.amazonaws.com"
DB_USER="admin"
DB_PASSWORD="password"
DB_NAME="chalice_db_" + DEPLOYMENT_ENV
conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        )
conn.autocommit = True
cursor = conn.cursor() 
query=("select * from Persons$")
cursor.execute(query)


