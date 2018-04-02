
import pymysql
import json


with open('team_all.json','r') as f:
    data = json.load(f)

print(len(data))


# 打开数据库连接
db = pymysql.connect(host="localhost", user="root",password="123456", db="nba")

# 使用cursor()方法获取操作游标
cur = db.cursor()


# 编写sql 查询语句  user 对应我的表名
insert_sql = "insert into team_info (id,name,city) values(%s,%s,%s)"
select_sql = "select * from team_info where id=%s"
try:
    for team in data:
        id = team['id']
        name = team['name']
        city = team['city']
        cur.execute(select_sql,(id,))
        res = cur.fetchall()
        if res is None or len(res) == 0:
            cur.execute(insert_sql,(id,name,city))  # 执行sql语句
    db.commit()
except Exception as e:
    raise e
finally:
    db.close()  # 关闭连接

