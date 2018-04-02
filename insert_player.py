
import pymysql
import json


with open('player_all_1.json','r') as f:
    data = json.load(f)

# print(len(data))


# 打开数据库连接
db = pymysql.connect(host="localhost", user="root",password="123456", db="nba")

# 使用cursor()方法获取操作游标
cur = db.cursor()

# height = data[0]['height'].split('-')
# print(height)
#
# tmp = (int(height[0])*12 + int(height[1])) * 2.54
# print(int(tmp) / 100)
#
# weight = data[0]['weight']
# print(weight)
#
# tmp2 = int(weight) * 0.4535924
# print(int(tmp2))

# 编写sql 查询语句  user 对应我的表名
# insert_sql = "insert into player_base (id,name,birthday,country,height,weight,draft,team_id,cloth_num,pos1,pos2) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
insert_sql = "insert into player_base (id,team_id) values(%s,%s)"
# select_sql = "select * from team_info where id=%s"
try:
    for team in data:
        id = team['player_id']
        # name = team['name']
        # birthday = team['birthday']
        # country = team['country']
        # tmp_hei = team['height'].split('-')
        # height = (int(tmp_hei[0])*12 + int(tmp_hei[1])) * 2.54
        # height = int(height) / 100
        #
        # tmp_wei = team['weight']
        # weight = int(tmp_wei) * 0.4535924
        # weight = int(weight)
        #
        # draft = team['draft']

        team_id = team['team_id']
        # cur.execute(select_sql,(id,))
        # res = cur.fetchall()
        # if res is None or len(res) == 0:
        cur.execute(insert_sql,(id,team_id))  # 执行sql语句
    db.commit()
except Exception as e:
    raise e
finally:
    db.close()  # 关闭连接

