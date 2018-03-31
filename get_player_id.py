# -*- coding: utf-8 -*-

from selenium import webdriver
from scrapy.selector import Selector
import json

# options = webdriver.FirefoxOptions()
# options.add_argument('-headless')

# driver = webdriver.Firefox(firefox_options=options)
# driver = webdriver.Firefox()

driver = webdriver.Chrome(executable_path="F:/tmp/chromedriver.exe")
url = 'https://stats.nba.com/players/list/'

driver.get(url)

players_ids = []

page = Selector(text=driver.page_source)


for player in page.css('div.stats-player-list.players-list ul.players-list__names li'):
    player_data = {}
    player_data['name'] = player.css('a::text').extract_first()
    player_data['id'] = player.css('a::attr(href)').re_first('.*/(\d+)/')

    players_ids.append(player_data)


file_name = 'player_id' + '.json'
with open(file_name, 'w') as f:
    f.write(json.dumps(players_ids))
    f.close()

print(len(players_ids))

driver.close()
