import os
import pymysql
DB_HOST="chalice-test.c4pa6qyxzm5o.us-east-2.rds.amazonaws.com"
DB_USER="admin"
DB_PASSWORD="password"
DB_NAME="chalice_db"


conn=pymysql.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        db = os.getenv('DB_NAME'),
        )
conn.autocommit = True
cursor = conn.cursor()
sql_file=open("artifact_folder/sale.sql")
sql_as_string=sql_file.read()
cursor.execute(sql_as_string)
cursor.execute("select * from Persons")