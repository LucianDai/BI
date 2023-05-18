# 将项目的区域获取，插入到项目区域维度表中
import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='admin',
                     database='bi',
                     charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 查询专利的阶段
sql = 'select province,  city from project'
cursor.execute(sql)
datas = cursor.fetchall()
list = []
i = 1
for data in datas:
    if data[1] not in list:
        list.append(data[1])
        sql = 'insert into project_region values' + "('" + str(i) + "'," + str(data).replace('(',"").replace(',',"',").replace("'',","',")
        print(sql)
        cursor.execute(sql)
        db.commit()
        i = i + 1
    else:
        pass
