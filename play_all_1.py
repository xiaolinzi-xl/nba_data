import json

with open('player_data1.json','r') as f:
    data1 = json.load(f)


with open('player_all.json','r') as f:
    data2 = json.load(f)


player_datas = []
for player1,player2 in zip(data1,data2):
    player_data = dict(player2)
    player_data['player_id'] = player1['player_id']
    # print(player_data)

    player_datas.append(player_data)
# print(data)

with open('player_all_1.json','w') as f:
    f.write(json.dumps(player_datas))
    f.close()