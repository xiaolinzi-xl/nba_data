import json
from selenium import webdriver
from scrapy.selector import Selector
import urllib.request

with open('teams_data.json', 'r') as f:
    data = json.load(f)


    # for team in data:
driver = webdriver.Firefox()

base_url = 'http://stats.nba.com/stats/commonteamroster?LeagueID=00&Season=2017-18&TeamID=%s'

player_datas = []

for team in data:
    url = base_url % team['id']
    driver.get(url)
    page = Selector(text=driver.page_source)
    res = {}
    player_data = page.css('#json::text').extract_first()
    res['data'] = player_data
    player_datas.append(res)

with open('player_data.json','w') as f:
    f.write(player_datas)
    f.close()

driver.close()
