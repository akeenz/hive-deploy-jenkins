import os
#create directory needed
mkdir artifact_folder
owner=akeenz
reponames=emr-hive-dataset
#write pr related info into a file named pr_info.json because we need the file later
curl -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/${owner}/${reponames}/pulls/${prnumber}/files > pr_info.json
PR_PROPERTY=$(curl -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/${owner}/${reponames}/pulls/${prnumber})
PR_BRANCH_NAME=$(echo $PR_PROPERTY | jq .head.ref | tr -d '"')
#change into the directory of the dataset repo [It must have been cloned at the inital stage when job was created]
echo "I will be cloning the dataset repo"
git clone https://github.com/${owner}/${reponames}.git
cd ${reponames}
git checkout ${PR_BRANCH_NAME}
echo "we are in ${PR_BRANCH_NAME} branch "


PR_BRANCH_DESTINATION=$(echo $PR_PROPERTY | jq .base.ref | tr -d '"')
IS_MERGED=$(echo $PR_PROPERTY | jq .merged | tr -d '"')
DEPLOYMENT_ENV=os.getenv('DEPLOYMENT_ENV')
#if this is a prod deployment, check if the PR has been merged into master
echo "Deploying into ${DEPLOYMENT_ENV}"
echo "This PR is Merging from ${PR_BRANCH_NAME} into ${PR_BRANCH_DESTINATION}"
echo "Is Code Merged already? And: ${IS_MERGED}"

if [[ "${DEPLOYMENT_ENV}" == "prod" ]]; then
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

#checkout the PR branch for
if [[ "${DEPLOYMENT_ENV}" == "prod" ]]; then
    git checkout $PR_BRANCH_DESTINATION
    echo "Currently checked into ${PR_BRANCH_DESTINATION} branch"
else
    git checkout $PR_BRANCH_NAME
    echo "Currently checked into ${PR_BRANCH_NAME} branch"
fi





#change into the directory of the dataset repo [It must have been cloned at the inital stage when job was created]
echo "I will be cloning the dataset repo"
git clone https://${GITHUB_TOKEN_USR}:${GITHUB_TOKEN_PSW}@github.intuit.com/golokunwolu/${dataset_dir}.git
cd ${dataset_dir}




cd ${reponames}
git checkout ${pr_branch_name}
echo "we are in ${pr_branch_name} branch "


