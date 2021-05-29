import os
import pymysql
DB_HOST="chalice-test.c4pa6qyxzm5o.us-east-2.rds.amazonaws.com"
DB_USER="admin"
DB_PASSWORD="password"
DB_NAME="chalice_db"



conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        )
conn.autocommit = True
cursor = conn.cursor()
sql_file=open("artifact_folder/sale.sql")
sql_as_string=sql_file.read()
cursor.execute(sql_as_string)
cursor.execute("select * from Persons")