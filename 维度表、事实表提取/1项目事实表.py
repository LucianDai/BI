# 将项目的各维度的相关信息获取，插入到项目事实表中
import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='admin',
                     database='bi',
                     charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = 'select project_categoryid,city,year,sp_org_id from project'
cursor.execute(sql)
datas = cursor.fetchall()
print(datas[0])
i = 1
for data in datas:
    sql1 = "select categorykey from category where category = '" + str(data[0]) + "'"
    sql2 = "select project_regionkey from project_region where city = '" + str(data[1]) + "'"
    sql3 = "select timekey from time_year where year = '" + str(data[2]) + "'"

    cursor.execute(sql1)
    a = cursor.fetchone()
    cursor.execute(sql2)
    b = cursor.fetchone()
    cursor.execute(sql3)
    c = cursor.fetchone()
    res = a+b+c

    res = str(res).replace('(',"'").replace(',',"','").replace(')',"'").replace(' ','')
    if data[3] ==None:
        sql = "insert into project_fact_table values('" + str(i) + "'," + str(res) + ",'" + str(0) + "')"
    else:
        sql = "insert into project_fact_table values('" + str(i) + "'," + str(res) + ",'" + str(data[3]) +"')"
    cursor.execute(sql)
    db.commit()
    i = i + 1
    # print(sql)


























# sql1 = 'select project_regionkey from project_region'
# sql2 = 'select project_categorykey from project_category'
# sql3 = 'select project_timekey from project_time'
# sql4 = 'select org_key from organisation'
#
# cursor.execute(sql1)
# data1 = cursor.fetchall()
#
# cursor.execute(sql2)
# data2 = cursor.fetchall()
#
# cursor.execute(sql3)
# data3 = cursor.fetchall()
#
# cursor.execute(sql4)
# data4 = cursor.fetchall()
# for data44 in data4:
#     print(data44[0])


# i = 1
#
#
# for data11 in data1:
#     for data22 in data2:
#         for data33 in data3:
#             for data44 in data4:
#                 sql = 'select project.project_id from project,project_category,project_region,project_time,organisation ' \
#                        'where project.project_id = project_category.project_categorykey and ' \
#                        '      project.project_id = project_region.project_regionkey and ' \
#                        '      project.sp_org_id = organisation.org_id and ' \
#                        '      project.project_id = project_time.project_timekey and ' \
#                        '      project_region.project_regionkey = ' + str(data11[0]) + ' and' \
#                        '      project_category.project_categorykey = ' + str(data22[0]) + ' and' \
#                        '      project_time.project_timekey = ' + str(data33[0])+ ' and' \
#                        '      project.sp_org_id = ' + str(data44[0])
#                 data =cursor.execute(sql)
#                 sql = 'insert into project_fact_table values(' + str(i) + ','+ str(data11[0]) + ',' + str(data22[0]) + ',' + str(data33[0])+ ','+str(data44[0]) + ','+ str(data) + ')'
#                 i = i + 1
#                 cursor.execute(sql)
#                 db.commit()
#                 print(data)