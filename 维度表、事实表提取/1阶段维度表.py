# 将专利的阶段获取，插入到成就阶段维度表中
import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='admin',
                     database='bi',
                     charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 查询专利的阶段
sql = 'select DISTINCT arch_stage from patent'
cursor.execute(sql)
data = cursor.fetchall()
i = 1
for data in data:
    data = (i,) + data
    sql = 'insert into stage values' + str(data).replace('(',"('").replace(',',"',")
    cursor.execute(sql)
    db.commit()
    i=i+1
    # print(str(data).replace('(',"('").replace(',',"',"))