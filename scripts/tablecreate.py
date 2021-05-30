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






#Using the Github API, find the souruce branch of the PR and set it to a variable called PR_BRANCH_NAME
PR_BRANCH_NAME=$(echo $PR_PROPERTY | jq .head.ref | tr -d '"')
PR_BRANCH_DESTINATION=$(echo $PR_PROPERTY | jq .base.ref | tr -d '"')
IS_MERGED=$(echo $PR_PROPERTY | jq .merged | tr -d '"')

#if this is a prod deployment, check if the PR has been merged into master
echo "Deploying into" + DEPLOYMENT_ENV
echo "This PR is Merging from" + PR_BRANCH_NAME + "into" + PR_BRANCH_DESTINATION
echo "Is Code Merged already? And:" + IS_MERGED

if [[ DEPLOYMENT_ENV == "prod" ]]; then
    if [[ "${PR_BRANCH_DESTINATION}" == "master" ]]; then
        if [[ "${IS_MERGED}" == "false" ]]; then
            echo "I cannot Deploy your Code into Prod until it is has successfully merged into the Master Branch"
            exit -1
        fi
    else
        echo "To Deploy into Prod,the PR must be attempting to Merge into master and not ${PR_BRANCH_DESTINATION}"
        exit -1
    fi
else
    echo "This will be a Non Prod Deployment"
fi
#change into the directory of the dataset repo [It must have been cloned at the inital stage when job was created]
echo "I will be cloning the dataset repo"
git clone https://${GITHUB_TOKEN_USR}:${GITHUB_TOKEN_PSW}@github.intuit.com/golokunwolu/${dataset_dir}.git
cd ${dataset_dir}

#checkout the PR branch for
if [[ "${DEPLOYMENT_ENV}" == "prod" ]]; then
    git checkout $PR_BRANCH_DESTINATION
    echo "Currently checked into ${PR_BRANCH_DESTINATION} branch"
else
    git checkout $PR_BRANCH_NAME
    echo "Currently checked into ${PR_BRANCH_NAME} branch"
fi

sql_file=open("artifact_folder/sale.sql")
sql_as_string=sql_file.read()
cursor.execute(sql_as_string)
#cursor.execute("select * from Persons$")






# import pandas as pd
# import pyodbc
# import numpy as np
 
# sql_conn = 'DRIVER=SQL Server Native Client 11.0; SERVER=desktop-r9rnma8; DATABASE=pollutin_db; Trusted_Connection=yes'

# sql_conn = pyodbc.connect(sql_conn)
 
query=("select * from Persons$")


sale = pd.read_sql(query, cursor)
 
sale.head(10)

