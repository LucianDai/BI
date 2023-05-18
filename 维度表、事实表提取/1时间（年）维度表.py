# 将专利的年月日分别获取，并插入到时间维度表中
from datetime import datetime

import pymysql
import pandas
db = pymysql.connect(host='localhost',
                     user='root',
                     password='admin',
                     database='bi',
                     charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 查询专利的年份
sql1 = 'select DISTINCT year from project'
sql2 = 'select DISTINCT year from sp_capital_scale'
sql3 = 'select id,year from listed_project'

cursor.execute(sql1)
datas1 = cursor.fetchall()
cursor.execute(sql2)
datas2 = cursor.fetchall()
cursor.execute(sql2)
datas3 = cursor.fetchall()
datas = datas1 + datas2 + datas3
# datas = str(datas)
print(type(datas))
list = []
i = 1
# 去重
for data in datas:
    if data not in list:
        list.append(data)
print(list)
for data in list:
    sql = "insert into time_year (timekey,year) values ('" + str(i) + "','" + str(data[0]) +  "')"
    cursor.execute(sql)
    db.commit()
    i = i + 1
    # print(sql)