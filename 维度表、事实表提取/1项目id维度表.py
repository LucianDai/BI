# 将项目的id获取，插入到项目维度表中
import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='admin',
                     database='bi',
                     charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 查询专利的阶段
sql = 'select project_id,project_id,sp_org_id from project'
cursor.execute(sql)
data = cursor.fetchall()
for data in data:
    sql = 'insert into project_id values' + str(data).replace(' ','0').replace('None','').replace('(',"('").replace(',',"','").replace(')',"')") + ";"
    cursor.execute(sql)
    db.commit()
    # print(str(data).replace(' ','0').replace('None','').replace('(',"('").replace(',',"','").replace(')',"')"))