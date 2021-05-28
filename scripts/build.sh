#create directory needed
mkdir artifact_folder
owner=akeenz
reponame=emr-data-hive
#write pr related info into a file named pr_info.json because we need the file later
curl -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/${owner}/{${reponame}/pulls/${prnumber}/files >> pr_info.json
git clone https://github.com/${owner}/${reponame}.git
python scripts/pybuild.py
