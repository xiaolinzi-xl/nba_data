import json

with open('season_base.json','r') as f:
    data = json.load(f)

print(len(data))

content = data[0]['data']

season_data = json.loads(content)
print(season_data['resultSets'][1]['headers'])
print(season_data['resultSets'][1]['rowSet'])