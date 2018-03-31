import json
# import urllib.request
# from urllib.error import HTTPError
from scrapy.selector import Selector
from selenium import webdriver

base_url = 'http://stats.nba.com/stats/playerdashboardbyyearoveryear?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=%s&PlusMinus=N&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&Split=yoy&VsConference=&VsDivision='
# hearder={
#    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
# }
#
# req = urllib.request.Request(url=url,headers=hearder)
#
# try:
#     response = urllib.request.urlopen(req)
#     html = response.read()
#     print(html)
# except HTTPError as e:
#     print(e.msg)

driver = webdriver.Chrome(executable_path="F:/tmp/chromedriver.exe")
#
# driver.get(url)
#

# print(html)

# with open('2.html','w') as f:
#     f.write(html)
#     f.close()

#
# with open('season_base.json','w') as f:
#     f.write(json.dumps(json.loads(content)))
# driver.close()

with open('player_all_1.json','r') as f:
    data = json.load(f)

# print(data)

season_datas = []

for player in data:
    url = base_url % player['player_id']
    driver.get(url)
    html = Selector(text=driver.page_source)
    content = html.css('pre::text').extract_first()

    player_data = json.dumps(json.loads(content))

    season_data = {}
    season_data['team_id'] = player['team_id']
    season_data['player_id'] = player['player_id']
    season_data['data'] = player_data

    season_datas.append(season_data)

with open('season_base.json','w') as f:
    f.write(json.dumps(season_datas))
    f.close()