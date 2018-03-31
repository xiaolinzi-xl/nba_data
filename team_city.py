import json
# import urllib.request
from selenium import webdriver
from scrapy.selector import Selector

with open('teams_data.json', 'r') as f:
    data = json.load(f)

# print(data)

base_url = "http://stats.nba.com/stats/teamdetails?teamID=%s"
# hearder={
#    'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# }
# req = urllib.request.Request(url,headers=hearder)
# response = urllib.request.urlopen(req)

driver = webdriver.Chrome(executable_path="F:/tmp/chromedriver.exe")

team_datas = []

for team in data:
    url = base_url % team['id']
    driver.get(url)
    html = Selector(text=driver.page_source)
    team_data = html.css("pre::text").extract_first()
    team_data = json.loads(team_data)
    city = team_data['resultSets'][0]['rowSet'][0][4]

    res = {}
    res['id'] = team['id']
    res['name'] = team['name']
    res['city'] = city

    team_datas.append(res)


with open("team_all.json", 'w') as f:
    f.write(json.dumps(team_datas))
    f.close()

driver.close()
