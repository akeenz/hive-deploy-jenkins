import os
import pymysql
import pandas as pd
env = os.getenv('deployment_env')
DB_HOST="chalice-test.c4pa6qyxzm5o.us-east-2.rds.amazonaws.com"
DB_USER="admin"
DB_PASSWORD="password"
DB_NAME="chalice_db_" + env
conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        )
conn.autocommit = True
cursor = conn.cursor()
dataset_dir=cg_dataset_test 
REPO_PULL=https://github.intuit.com/api/v3/repos/golokunwolu/${dataset_dir}/pulls/
PR_PROPERTY=$(curl -u "${GITHUB_TOKEN_USR}:$GITHUB_TOKEN_PSW" -H "Accept: application/vnd.github.v3+json" ${REPO_PULL}${PR_NUMBER})
PR_VALIDITY=$(echo $PR_PROPERTY | jq .message | tr -d '"')
DATASET_CLONE_LINK = "https://${GITHUB_TOKEN_USR}:${GITHUB_TOKEN_PSW}@github.intuit.com/golokunwolu/${dataset_dir}.git"




# #Delete files.folders if they exist
# if [ -f pr_${PR_NUMBER}_pull_info.json ]; then
#     rm -rf pr_${PR_NUMBER}_pull_info.json
#     echo "Deleting pr_${PR_NUMBER}_pull_info.json ..."
# fi
# if [ -d pr_${PR_NUMBER}_related_objects ]; then
#     rm -rf pr_${PR_NUMBER}_related_objects
#     echo "Deleting pr_${PR_NUMBER}_related_objects ..."
# fi

# if [ -f pr_${PR_NUMBER}_db_object_grant.hql ]; then
#     rm -rf pr_${PR_NUMBER}_db_object_grant.hql
#     echo "Deleting pr_${PR_NUMBER}_db_object_grant.hql ..."
# fi
# if [ -d ${dataset_dir} ]; then
#     echo "Deleting ${dataset_dir} ..."
#     rm -rf ${dataset_dir}
# fi

# #Create files and directories needed for deployment
# touch pr_${PR_NUMBER}_pull_info.json
# mkdir pr_${PR_NUMBER}_related_objects/views
# mkdir pr_${PR_NUMBER}_related_objects/tables
# touch pr_${PR_NUMBER}_related_objects/tables/db_object_grant.hql

# #quickly copy grant file into pr__related_files_folder_tables
# cp scripts-exec/grant.sql pr_${PR_NUMBER}_related_files_folder_tables

# #Use Github API to get the current PR properties and Write to the json file created above
# echo "I will be writing all changes related to PR ${PR_NUMBER} into pr_${PR_NUMBER}_pull_info.json"
# curl -u "${GITHUB_TOKEN_USR}:${GITHUB_TOKEN_PSW}" -H "Accept: application/vnd.github.v3+json" ${REPO_PULL}${PR_NUMBER}/files >> pr_${PR_NUMBER}_pull_info.json

# #Using the Github API, find the souruce branch of the PR and set it to a variable called PR_BRANCH_NAME
# PR_BRANCH_NAME=$(echo $PR_PROPERTY | jq .head.ref | tr -d '"')
# PR_BRANCH_DESTINATION=$(echo $PR_PROPERTY | jq .base.ref | tr -d '"')
# IS_MERGED=$(echo $PR_PROPERTY | jq .merged | tr -d '"')

# #if this is a prod deployment, check if the PR has been merged into master
# echo "Deploying into ${DEPLOYMENT_ENV}"
# echo "This PR is Merging from ${PR_BRANCH_NAME} into ${PR_BRANCH_DESTINATION}"
# echo "Is Code Merged already? And: ${IS_MERGED}"

# if [[ "${DEPLOYMENT_ENV}" == "prod" ]]; then
#     if [[ "${PR_BRANCH_DESTINATION}" == "master" ]]; then
#         if [[ "${IS_MERGED}" == "false" ]]; then
#             echo "I cannot Deploy your Code into Prod until it is has successfully merged into the Master Branch"
#             exit -1
#         fi
#     else
#         echo "To Deploy into Prod,the PR must be attempting to Merge into master and not ${PR_BRANCH_DESTINATION}"
#         exit -1
#     fi
# else
#     echo "This will be a Non Prod Deployment"
# fi

# #change into the directory of the dataset repo [It must have been cloned at the inital stage when job was created]
# echo "I will be cloning the dataset repo"
# git clone https://${GITHUB_TOKEN_USR}:${GITHUB_TOKEN_PSW}@github.intuit.com/golokunwolu/${dataset_dir}.git
# cd ${dataset_dir}

# #checkout the PR branch for
# if [[ "${DEPLOYMENT_ENV}" == "prod" ]]; then
#     git checkout $PR_BRANCH_DESTINATION
#     echo "Currently checked into ${PR_BRANCH_DESTINATION} branch"
# else
#     git checkout $PR_BRANCH_NAME
#     echo "Currently checked into ${PR_BRANCH_NAME} branch"
# fi

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

