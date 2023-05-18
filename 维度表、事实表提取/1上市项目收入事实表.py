# 将上市公司项目的各维度的相关信息获取，插入到上市公司项目收入事实表中
import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='admin',
                     database='bi',
                     charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = 'select year,org_id,project_income from listed_project'
cursor.execute(sql)
datas = cursor.fetchall()
print(datas[0][0])
i = 1
for data in datas:
    sql1 = "select timekey from time_year where year = '" + str(data[0]) + "'"
    cursor.execute(sql1)
    a = cursor.fetchone()
    res = a + data
    # print(res)
    sql = "insert into listed_project_fact_table values('" + str(i) + "','" + str(res[0]) + "','" + str(res[2]) + "','" + str(res[3]) + "')"
    cursor.execute(sql)
    db.commit()
    # print(sql)
    i = i + 1
























# sql1 = 'select listed_project_timekey from listed_project_time'
# sql2 = 'select org_id from organisation'
#
#
# cursor.execute(sql1)
# data1 = cursor.fetchall()
#
# cursor.execute(sql2)
# data2 = cursor.fetchall()
#
# i = 1
# for data11 in data1:
#     for data22 in data2:
#         sql = 'select project_income from listed_project,listed_project_time,organisation ' \
#               'where listed_project.id = listed_project_time.listed_project_timekey and ' \
#               '      listed_project.org_id = organisation.org_id and ' \
#               '      listed_project.id = ' + str(data11[0]) + ' and' \
#               '      organisation.org_id = ' + str(data22[0])
#         cursor.execute(sql)
#         data = cursor.fetchone()
#
#         if str(data) == 'None':
#             sql = 'insert into listed_project_fact_table values(' + str(i) + ',' + str(data11[0]) + ',' + str(data22[0]) + ','  + '0' + ')'
#         if str(data) != 'None':
#             sql = 'insert into listed_project_fact_table values(' + str(i) + ',' + str(data11[0]) + ',' + str(data22[0]) + ',' + str(data[0]) + ')'
#
#         i = i + 1
#         cursor.execute(sql)
#         db.commit()
#         # print(str(data))
#         # print(sql)
