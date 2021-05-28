#create directory needed
mkdir artifact_folder
owner=akeenz
reponames=emr-hive-dataset
#write pr related info into a file named pr_info.json because we need the file later
curl -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/${owner}/${reponames}/pulls/${prnumber}/files >> pr_info.json
git clone https://github.com/${owner}/${reponames}.git
python3 scripts/pybuild.py
