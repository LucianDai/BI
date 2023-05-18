# 将支持资金的各维度的相关信息获取，插入到支持资金事实表中
import pymysql
from unicodedata import decimal

db = pymysql.connect(host='localhost',
                     user='root',
                     password='admin',
                     database='bi',
                     charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = 'select project.city,project.project_categoryid,sp_capital_scale.year,project.project_id,project.sp_org_id,sp_capital_scale from sp_capital_scale,project ' \
      'where sp_capital_scale.project_id = project.project_id'
cursor.execute(sql)
datas = cursor.fetchall()
# print(datas)
# print(sql)
i = 1
for data in datas:
    sql1 = "select project_regionkey from project_region where city = '" + str(data[0]) + "'"
    sql2 = "select categorykey from category where category = '" + str(data[1]) + "'"
    sql3 = "select timekey from time_year where year = '" + str(data[2]) + "'"
    sql4 = "select project_key from project_id where project_id = '" + str(data[3]) + "'and "\
           "sp_org_id = '" + str(data[4]) + "'"
    cursor.execute(sql1)
    a = cursor.fetchone()
    cursor.execute(sql2)
    b = cursor.fetchone()
    cursor.execute(sql3)
    c = cursor.fetchone()
    cursor.execute(sql4)
    d = cursor.fetchone()
    res = a+b+c+d
    res = str(res).replace('(',"'").replace(',',"','").replace(')',"'").replace(' ','')

    print(res)

    sql = "insert into sp_capital_scale_fact_table values('" + str(i) + "'," + res + ",'" + str(data[5]) + "')"
    data = cursor.execute(sql)
    db.commit()
    i = i + 1
    # cursor.execute(sql1)
    # data1 = cursor.fetchone()
    # print(data1[0])
    # print('----------------')











# sql1 = 'select project_regionkey from project_region'
# sql2 = 'select project_categorykey from project_category'
# sql3 = 'select sp_capital_scale_timekey from sp_time'
# sql4 = 'select project_key from project_id'
# sql5 = 'select org_key from organisation'
#
# cursor.execute(sql1)
# data1 = cursor.fetchall()
# # print(data1[0])
#
# cursor.execute(sql2)
# data2 = cursor.fetchall()
# # print(data2[0])
#
# cursor.execute(sql3)
# data3 = cursor.fetchall()
# # print(data3[0])
#
# cursor.execute(sql4)
# data4 = cursor.fetchall()
# # print(data4[0])
#
# cursor.execute(sql5)
# data5 = cursor.fetchall()
# # print(data5[0])
#
# i = 1
#
# for data11 in data1:
#     for data22 in data2:
#         for data33 in data3:
#             for data44 in data4:
#                 for data55 in data5:
#                     sql = 'select sp_capital_scale.sp_capital_scale from sp_capital_scale,project_id,project_category,project_region,sp_time,organisation ' \
#                            'where sp_capital_scale.project_id = project_id.project_key and ' \
#                            '      sp_capital_scale.project_id = project_category.project_categorykey and ' \
#                            '      sp_capital_scale.project_id = project_region.project_regionkey and ' \
#                            '      sp_capital_scale.sp_id = sp_time.sp_capital_scale_timekey and ' \
#                            '      project_id.sp_org_id = organisation.org_id and' \
#                            '      project_region.project_regionkey = ' + str(data11[0]) + ' and ' \
#                            '      project_category.project_categorykey = ' + str(data22[0])+ ' and ' \
#                            '      sp_time.sp_capital_scale_timekey = ' + str(data33[0]) + ' and ' \
#                            '      project_id.project_key = ' + str(data44[0]) + ' and ' \
#                            '      organisation.org_key = '+ str(data55[0])
#                     cursor.execute(sql)
#                     data = cursor.fetchone()
#                     # print(str(data[0]))
#
#                     if str(data) == 'None':
#                         sql = 'insert into sp_capital_scale_fact_table values(' + str(i) + ',' + str(data11[0]) + ',' + str(data22[0]) + ',' + str(data33[0]) + ','+ str(data44[0]) + ','+ str(data55[0]) + ','+ '0' + ')'
#                     if str(data) != 'None':
#                         sql = 'insert into sp_capital_scale_fact_table values(' + str(i) + ',' + str(data11[0]) + ',' + str(data22[0]) + ',' + str(data33[0]) + ','+ str(data44[0]) + ','+ str(data55[0]) + ','+ str(data[0]) + ')'
#
#                     i = i + 1
#                     data = cursor.execute(sql)
#                     db.commit()
#                     # print(data)
#                     # print(sql)
