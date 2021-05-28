#create directory needed
mkdir artifact_folder
owner=akeenz
reponames=emr-hive-dataset
#write pr related info into a file named pr_info.json because we need the file later
curl -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/${owner}/${reponames}/pulls/${prnumber}/files > pr_info.json
pr_property = $(curl -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/${owner}/${reponames}/pulls/${prnumber})
pr_branch_name = $(echo ${pr_property} | jq .head.ref | tr -d '"')
git clone https://github.com/${owner}/${reponames}.git
cd ${reponames}
git checkout ${pr_branch_name}
echo "we are in ${pr_branch_name} branch "
python3 scripts/pybuild.py

