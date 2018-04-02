
import json

with open('player_all_1.json','r') as f:
    data = json.load(f)
    f.close()

player_set = set()

for player in data:
    id = player['player_id']
    player_set.add(id)

print("data has ",len(data))

print("actual has ",len(player_set))