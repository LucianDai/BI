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
sql1 = 'select DISTINCT arch_starttime from patent'
sql2 = 'select DISTINCT arch_endtime from patent'

cursor.execute(sql1)
datas1 = cursor.fetchall()
cursor.execute(sql2)
datas2 = cursor.fetchall()

datas4 = cursor.fetchall()
datas = datas1 + datas2
list = []
# print(type(datas))
i = 1
# 去重
for data in datas:
    if data not in list:
        list.append(data)
for data in datas:
    if str(data[0]) == 'None':
        pass
    else:
        sql = "insert into time_year_and_month_and_day (timekey,time,year_of_time,month_of_time,day_of_time) values ('" + str(i) + "','" + str(data[0]) + "','" + str(data[0].year) + "','" + str(data[0].month) + "','" +str(data[0].day) + "')"
        cursor.execute(sql)
        db.commit()
        i = i + 1
