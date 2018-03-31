
import json
import urllib.request
from scrapy.selector import Selector

with open('player_data1.json','r') as f:
    data = json.load(f)

# print(data)

base_url = 'http://stats.nba.com/player/%s/'

player_datas = []

for player in data:
    url = base_url % player['player_id']
    response = urllib.request.urlopen(url)
    html = Selector(text=response.read())

    country = html.css('div.player-stats__prior span::text').re_first('.*?/(.*)')
    draft = html.css('div.player-stats__draft span::text').extract_first()
    birthday = html.css('div.player-stats__birthdate span::text').extract_first()

    player_data = {}
    player_data['team_id'] = player['team_id']
    player_data['player_id'] = player['player_id']
    player_data['name'] = player['name']
    player_data['clothes_num'] = player['clothes_num']
    player_data['pos'] = player['pos']
    player_data['height'] = player['height']
    player_data['weight'] = player['weight']
    player_data['country'] = country
    player_data['birthday'] = birthday
    player_data['draft'] = draft

    player_datas.append(player_data)

with open('player_all.json','w') as f:
    f.write(json.dumps(player_datas))
    f.close()
