import json
import os
path = 'pr_info.json'
# Opening JSON file
f = open(path,)
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
#  print(data('filename'))
for i in data:
    file = i['filename']
    os.system('cp emr-data-hive/' + file + ' artifact_folder') 
  