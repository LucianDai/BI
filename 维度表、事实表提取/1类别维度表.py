# 将专利的类别获取，插入到成就类别维度表中
import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='admin',
                     database='bi',
                     charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 查询专利的阶段
sql1 = 'select DISTINCT arch_categoryid from patent'
sql2 = 'select DISTINCT project_categoryid from project'

cursor.execute(sql1)
data1 = cursor.fetchall()
cursor.execute(sql2)
data2 = cursor.fetchall()
datas = data1 + data2
i = 1
for data in datas:
    data = (i,) + data
    sql = 'insert into category values' + str(data).replace('(',"('").replace(',',"',")
    cursor.execute(sql)
    db.commit()
    i = i + 1
    # print(str(data).replace(',)',')'))
    # data = (i,) + data
    print(str(data).replace('(',"('").replace(',',"',"))