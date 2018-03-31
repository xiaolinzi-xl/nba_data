import json

with open('player_data.json','r') as f:
    data = json.load(f)

# team = data[0]['data']
#
# print(team)

# 使用 loads 方法将字符串转换成字典
# team_player = json.loads(team)

# print(team_player['resultSets'][0]['rowSet'])

player_datas = []

for team in data:
    team_data = team['data']
    team_player = json.loads(team_data)
    for player in team_player['resultSets'][0]['rowSet']:
        player_data = {}
        player_data['team_id'] = player[0]
        player_data['name'] = player[3]
        player_data['clothes_num'] = player[4]
        player_data['pos'] = player[5]
        player_data['height'] = player[6]
        player_data['weight'] = player[7]
        player_data['player_id'] = player[-1]

        player_datas.append(player_data)

with open('player_data1.json','w') as f:
    f.write(json.dumps(player_datas))
    f.close()
print(len(player_datas))