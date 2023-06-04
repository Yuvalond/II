import json

with open('II\Oznokom praktika\BlockF\SerealizeData\data.json') as file:
    data = json.loads(file.read())
    
if isinstance(data, dict):
    data = [data]
  
for i in data:
    if i['id_user'] == 277267389:
        group = i['group']