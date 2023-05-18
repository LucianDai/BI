# 将专利的各维度的相关信息获取，插入到专利事实表中
import pymysql
db = pymysql.connect(host='localhost',user='root',password='admin',database='bi',charset='utf8')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = 'select arch_categoryid,arch_stage,arch_starttime,org_id from patent'
cursor.execute(sql)
datas = cursor.fetchall()
# print(type(data))
# print(data[0][1])
i=1
for data in datas:
    sql1 = "select categorykey from category where category = '" + data[0] + "'"
    sql2 = "select stagekey from stage where stage = '" + data[1] + "'"
    sql3 = "select timekey from time_year_and_month_and_day where time = '" + str(data[2]) + "'"

    cursor.execute(sql1)
    a = cursor.fetchone()
    cursor.execute(sql2)
    b = cursor.fetchone()
    cursor.execute(sql3)
    c = cursor.fetchone()
    res = a+b+c
    # print(type(res))
    res = str(res).replace('(',"'").replace(',',"','").replace(')',"'").replace(' ','')
    if data[3] == None:
        sql = "insert into patent_fact_table values('" + str(i) +"'," + res + ",'" + str(0) +"')"
    else:
        sql = "insert into patent_fact_table values('" + str(i) +"'," + res + ",'" + str(data[3]) +"')"
    data = cursor.execute(sql)
    db.commit()
    i = i + 1
    # print(sql)









# sql1 = 'select arch_stagekey from arch_stage'
# sql2 = 'select arch_categorykey from arch_category'
# sql3 = 'select arch_timekey from arch_time'
# sql4 = 'select org_key from organisation'
# cursor.execute(sql1)
# data1 = cursor.fetchall()
# cursor.execute(sql2)
# data2 = cursor.fetchall()
# cursor.execute(sql3)
# data3 = cursor.fetchall()
# cursor.execute(sql4)
# data4 = cursor.fetchall()
# i = 1
# for data11 in data1:
#     for data22 in data2:
#         for data33 in data3:
#             for data44 in data4:
#                 sql = 'select patent.arch_id from patent,arch_category,arch_stage,arch_time,organisation ' \
#                        'where patent.arch_id = arch_stage.arch_stagekey and ' \
#                        'patent.arch_id = arch_categorykey and ' \
#                        'patent.arch_id = arch_time.arch_timekey and ' \
#                        'patent.org_id = organisation.org_id and ' \
#                        'arch_stagekey = ' + str(data11[0]) + ' and ' \
#                        'arch_categorykey = ' + str(data22[0]) + ' and ' \
#                        'arch_timekey = ' + str(data33[0]) + ' and ' \
#                        'patent.org_id = ' + str(data44[0])
#
#                 data = cursor.execute(sql)
#                 sql = 'insert into patent_fact_table values(' + str(i) + ','+ str(data11[0]) + ',' + str(data22[0]) + ',' + str(data33[0])+ ','+str(data44[0]) + ','+ str(data) + ')'
#                 i = i + 1
#                 data = cursor.execute(sql)
#                 db.commit()
