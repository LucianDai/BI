# 将公司的相关信息获取，插入到机构维度表中
import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='admin',
                     database='bi',
                     charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 查询公司的相关信息
sql = 'select org_id,org_id,org_name,org_categoryid,org_countrycode,org_provincecode,org_citycode,main_product from company'
cursor.execute(sql)
data = cursor.fetchall()
for data in data:
    sql = 'insert into organisation values' + str(data).replace(' ','').replace('(',"('").replace(",","','").replace("''","'") + ";"
    cursor.execute(sql)
    db.commit()
    # print(str(data).replace(' ','').replace('(',"('").replace(",","','").replace("''","'"))