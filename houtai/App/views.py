import calendar
import json
import uuid

import numpy as np
import pymysql
from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from py2neo import Graph
# from requests import request

from App import models, authenticate, login, logout


class BaseView(View):
    def get(self, request, module, *args, **kwargs):

        if module == 'fill':
            return SysView.fill(request)
    def post(self, request, module, *args, **kwargs):

        if module == 'login':
            return SysView.login(request)
        elif module == 'register':
            return SysView.register(request)


    def successData(data, msg='处理成功'):
        resl = {'code':0,'msg':msg,'data':data}
        # return resl
        return HttpResponse(json.dumps(resl),content_type='application/json;charset=UTF-8')

'''
系统处理
'''
class SysView(BaseView):
    def get(self, request, module, *args, **kwargs):
        if module == 'login':
            return SysView.login(request)
        elif module == 'register':
            return SysView.register(request)
        elif module == 'fillInForm':
            return SysView.fillInForm(request)
        elif module == 'modify_information':
            return SysView.modify_information(request)
        elif module == 'modify_password':
            return SysView.modify_password(request)   
        elif module == 'get_information':
            return SysView.get_information(request)     
         
    def post(self, request, module, *args, **kwargs):
        if module == 'login':
            return SysView.login(request)
        elif module == 'register':
            return SysView.register(request)
        elif module == 'fillInForm':
            return SysView.fillInForm(request)
        elif module == 'modify_information':
            return SysView.modify_information(request)
        elif module == 'modify_password':
            return SysView.modify_password(request)    
        elif module == 'get_information':
            return SysView.get_information(request)      
    def search_password(username):
        sql = "select password from info where username = '" + username + "'"
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='user',
                             charset='utf8')

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        cursor.execute(sql)
        password = cursor.fetchone()
        if password is not None:
            return password[0]
        else:
            return 0

    def search_power(username):
        sql = "select power from info where username = '" + username + "'"
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='user',
                             charset='utf8')

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        cursor.execute(sql)
        power = cursor.fetchone()

        return power[0]

    def new_user(username, password, power=0):
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='user',
                             charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "select id from info where username = '" + username + "'"
        cursor.execute(sql)
        data = cursor.fetchone()
        # print(data)
        if data is None:
            sql = "insert into info(username,password,power) values('" + username + "','" + password + "','" + str(
                power) + "')"
            cursor.execute(sql)
            db.commit()
            return 1
        else:
            return 0

    def fillInForm(request):
        sql = 'select id,username,city,mailAddress,Address,phoneNumber,remark from info'
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='user',
                             charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor

        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()

        return JsonResponse({
                    'status': 1,
                    'message': data,
                })
    
    def login(request):
        if request.method == "GET":
            username = request.GET.get('username')
            password = request.GET.get('password')
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

        password_this = SysView.search_password(username)
        print(password_this)

        if password_this is None:
            return JsonResponse({
                    'status': 0,
                    'message': "用户名不存在",
                    'username': username
                })

        elif password_this == password:
            power_this = SysView.search_power(username)
            if power_this == 0:
                return JsonResponse({
                    "status": 1,
                    "message": "用户登录成功",
                    "username": username
                })

            elif power_this == 1:
                return JsonResponse({
                    "status": 1,
                    "message": "管理员登录成功",
                    "username": username
                })

        elif password_this != password:
            return JsonResponse({
                "status": 2,
                "message": "用户名或密码错误",
                "username": username
            })

    def register(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

        if request.method == "GET":
            username = request.GET.get('username')
            password = request.GET.get('password')

        code = SysView.new_user(username,password)
        if code == 0:
            return JsonResponse({
                "status": 0,
                "message": "用户名已存在",
                "username": username
            })
        else:
            return JsonResponse({
                "status": 1,
                "message": "注册成功",
                "username": username
            })
    
    def modify_password(request):
        if request.method == "POST":
            username = request.POST.get('username')
            old_password = request.POST.get('old_password')
            new_password = request.POST.get('new_password')
        if request.method == "GET":
            username = request.GET.get('username')
            old_password = request.GET.get('old_password')
            new_password = request.GET.get('new_password')

        password = SysView.search_password(username)

        if password != old_password:
            return JsonResponse({
                    "status": 0,
                    "message": "原密码输入错误",
                    "username": username
                })

        if password == old_password:
            sql = "update info set password = '" + new_password + "' where username = '" + username + "'"
            db = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='user',
                             charset='utf8')
            # 使用 cursor() 方法创建一个游标对象 cursor

            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            return JsonResponse({
                    "status": 1,
                    "message": "修改成功！",
                    "username": username
                })
    
    def modify_information(request):
        if request.method == "POST":
            action = request.POST.get('action')
            username = request.POST.get('username')
            phoneNumber = request.POST.get('phoneNumber')
            mailAddress = request.POST.get('mailAddress')
            city = request.POST.get('city')
            Address = request.POST.get('Address')
            remark = request.POST.get('remark')        
        
        if request.method == "GET":
            action = request.GET.get('action')
            username = request.GET.get('username')
            phoneNumber = request.GET.get('phoneNumber')
            mailAddress = request.GET.get('mailAddress')
            city = request.GET.get('city')
            Address = request.GET.get('Address')
            remark = request.GET.get('remark')  

        db = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='user',
                             charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        if action == 'del':
            sql = "delete from info where username = '" + username + "'"
            cursor.execute(sql)
            db.commit()
            
            return JsonResponse({
                                "status": 1,
                                "message": "删除成功！",
                                "username": username
                            })
        
        if action == 'insert':
            sql = "select id from info where username = '" + username + "'"
            cursor.execute(sql)
            data = cursor.fetchone()
            if data is None:
                sql = "insert into info(username,password,power,phoneNumber,mailAddress,city,Address,remark) values('" + username + "','123456','0','" + phoneNumber + "','" + mailAddress + "','" + city + "','" + Address + "','" + remark + "')"
                cursor.execute(sql)
                db.commit()
                return JsonResponse({
                    "status": 1,
                    "message": "添加成功！",
                    "username": username
                })
            else:
                return JsonResponse({
                    "status": 0,
                    "message": "用户名已存在！",
                    "username": username
                })

        if action == 'update':
            sql = "update info set phoneNumber = '" + phoneNumber + "',city = '" + city + "',mailAddress = '"+ mailAddress + "',city = '" + city + "',Address = '" + Address + "',remark = '" + remark + "' where username = '" + username + "'"
            cursor.execute(sql)
            db.commit()
            return JsonResponse({
                    "status": 1,
                    "message": "修改成功！",
                    "username": username
                })
        
    def get_information(request):
        if request.method == "POST":
            username = request.POST.get('username')

        if request.method == "GET":
            username = request.GET.get('username')

        sql = "select id,username,city,mailAddress,Address,phoneNumber,remark from info where username = '" + username + "'"

        db = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='user',
                             charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()

        return JsonResponse({
                    'status': 1,
                    'message': '查询成功！',
                    'data': data
                })
'''
竞争对手
'''
class duishou(BaseView):
    def get(self,request,module,*args,**kwargs):
        if module == 'chazhao':
            return duishou.chazhao(request)
        elif module == 'xuanze':
            return duishou.xuanze()

    def post(self,request,module,*args,**kwargs):
        if module == 'chazhao':
            return duishou.chazhao(request)
        elif module == 'xuanze':
            return duishou.xuanze()

    def xuanze(request):
        company1 = request.POST.get('company1')
        company2 = request.POST.get('company2')
        year = 2020
        return keshihua.keshihua(company1,company2,year)

    def find_product_by_company(g, company):
        # 查询某家公司生产的产品
        product = ''
        query = "MATCH(n1:Corporation{name:'" + company + "'})-[r:生产]->(n2) RETURN n2"
        result = g.run(query)
        for record in result:
            tail_node = record['n2']
            product = tail_node['name']
            print("产品为" + product)
            print('-------------------------------')

        return product

    def find_next_product_by_product(g, product):
        # 查询某个产品下游的产品
        product_list = []
        query = "MATCH(n1:Product{name:'" + product + "'})-[r:原材料]->(n2) RETURN n2"
        result = g.run(query)
        next_product = ""
        for record in result:
            tail_node = record['n2']
            next_product = tail_node['name']
            product_list.append(next_product)
            print("下游产品为" + next_product)
            print('-------------------------------')
        return product_list

    def find_pre_product_by_product(g, product):
        # 查询某个产品上游的产品
        product_list = []
        query = "MATCH(n1:Product)-[r:原材料]->(n2{name:'" + product + "'}) RETURN n1"
        result = g.run(query)
        for record in result:
            head_node = record['n1']
            pre_product = head_node['name']
            product_list.append(pre_product)
            print("上游产品为" + pre_product)
            print('-------------------------------')
        return product_list

    def find_company_by_product(g, product):
        # 通过某个产品查询对应的公司
        list = []
        query = "MATCH(n1:Corporation)-[r:生产]->(n2{name:'" + product + "'}) RETURN n1"
        result = g.run(query)
        for record in result:
            tail_node = record['n1']
            # print(tail_node['name'])
            list.append(tail_node['name'])
        return list

    def chazhao(request):
        if request.method == "GET":
            company1 = request.GET.get('company1')
        if request.method == "POST":
            company1 = request.POST.get('company1')
        g = Graph('http://localhost:7474/', user='neo4j', password='123456789', name='neo4j')
        next_company = []  # 下游
        local_company = []  # 同业
        pre_company = []  # 上游
        # print(type(duishou.find_product_by_company(g, company1)))
        product1 = duishou.find_product_by_company(g, company1)

        next = duishou.find_next_product_by_product(g, product1)
        print(type(product1))
        print(type(next))
        pre = duishou.find_pre_product_by_product(g, product1)
        # 寻找下游公司
        for i in range(len(next)):
            next_com = duishou.find_company_by_product(g, next[i])
            for j in range(len(next_com)):
                next_company.append(next_com[j])
        print(next_company)
        # 寻找同业公司
        local_company = duishou.find_company_by_product(g, product1)
        print(local_company)
        # 寻找上游公司
        for i in range(len(pre)):
            pre_com = duishou.find_company_by_product(g, pre[i])
            for j in range(len(pre_com)):
                pre_company.append(pre_com[j])
        print(pre_company)
        if len(next_company) == 0:
            next_company = ['未找到下游公司']
        if len(local_company) == 0:
            local_company = ['未找到同业公司']
        if len(pre_company) == 0:
            pre_company = ['未找到上游公司']
        data = {'n1': next_company, 'n2': local_company, 'n3': pre_company, 'company': company1}
        return SysView.successData(data)

'''
可视化
'''
class keshihua(BaseView):
    companyNow = []
    def get(self,request,module,*args,**kwargs):
        if module == 'keshihua':
            return keshihua.keshihua(request)
        if module == 'get_list':
            return keshihua.get_list(request)


    def post(self,request,module,*args,**kwargs):

        if module == 'keshihua':
            return keshihua.keshihua(request)
        if module == 'get_list':
            return keshihua.get_list(request)

    # 查询某两家公司在某天的专利数量(可用)
    def count_patent_of_two_company_in_a_certain_day(cursor, company1, company2, year, month, day):
        sql1 = 'select patent_fact_table.id from patent_fact_table,time_year_and_month_and_day,organisation ' \
               'where patent_fact_table.timekey = time_year_and_month_and_day.timekey and ' \
               '      patent_fact_table.org_key = organisation.org_id and' \
               "      organisation.org_name = '" + company1 + "'and" \
               "      time_year_and_month_and_day.year_of_time = '" + year + "'and" \
               "      time_year_and_month_and_day.month_of_time = '" + month + "'and" \
               "      time_year_and_month_and_day.day_of_time = " + day
        sql2 = 'select patent_fact_table.id from patent_fact_table,time_year_and_month_and_day,organisation ' \
               'where patent_fact_table.timekey = time_year_and_month_and_day.timekey and ' \
               '      patent_fact_table.org_key = organisation.org_id and' \
               "      organisation.org_name = '" + company2 + "'and" \
               "      time_year_and_month_and_day.year_of_time = '" + year + "'and" \
               "      time_year_and_month_and_day.month_of_time = '" + month + "'and" \
               "      time_year_and_month_and_day.day_of_time = " + day
        data1 = cursor.execute(sql1)
        data2 = cursor.execute(sql2)

        return data1,data2

    # 查询某两家公司在某年某月的专利数量
    def count_patent_of_two_company_in_a_certain_year_and_month(cursor, company1, company2, year, month):
        data1 = []
        data2 = []
        # 如果是大月
        if int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7 or int(month) == 8 or int(
                month) == 10 or int(month) == 12:
            for i in range(1, 32):
                res1, res2 = keshihua.count_patent_of_two_company_in_a_certain_day(cursor, company1, company2, year, month, str(i))
                data1.append(res1)
                data2.append(res2)
            res1 = np.sum(data1)
            res2 = np.sum(data2)
            return res1, res2
        check_year = calendar.isleap(int(year))
        # 如果是闰年
        if check_year == True and int(month) == 2:
            for i in range(1, 30):
                res1, res2 = keshihua.count_patent_of_two_company_in_a_certain_day(cursor, company1, company2, year, month, str(i))
                data1.append(res1)
                data2.append(res2)
            res1 = np.sum(data1)
            res2 = np.sum(data2)
            return res1, res2
            # 如果不是闰年
        if check_year == False and int(month) == 2:
            for i in range(1, 29):
                res1, res2 = keshihua.count_patent_of_two_company_in_a_certain_day(cursor, company1, company2, year, month, str(i))
                data1.append(res1)
                data2.append(res2)
            res1 = np.sum(data1)
            res2 = np.sum(data2)
            return res1, res2
        else:
            # 如果是小月
            for i in range(1, 31):
                res1, res2 = keshihua.count_patent_of_two_company_in_a_certain_day(cursor, company1, company2, year, month, str(i))
                data1.append(res1)
                data2.append(res2)
            res1 = np.sum(data1)
            res2 = np.sum(data2)
            return res1, res2
    # 查询某两家公司在某年的专利数量(可用)
    def count_patent_of_two_company_in_a_certain_year(cursor, company1, company2, year):
        data1 = []
        data2 = []
        data3 = []
        data4 = []
        for i in range(1, 13):
            res1, res2 = keshihua.count_patent_of_two_company_in_a_certain_year_and_month(cursor, company1, company2, year, str(i))
            data1.append(res1)
            data2.append(res2)
            data3.append(str(res1))
            data4.append(str(res2))

        res1 = int(np.sum(data1))
        res2 = int(np.sum(data2))
        return res1,res2,data3,data4
        # sql1 = 'select patent_fact_table.id from patent_fact_table,time_year_and_month,organisation ' \
        #        'where patent_fact_table.timekey = time_year_and_month.timekey and ' \
        #        '      patent_fact_table.org_key = organisation.org_id and' \
        #        "      organisation.org_name = '" + company1 + "'and" \
        #        '      time_year_and_month.year_of_time = ' + year
        # sql2 = 'select patent_fact_table.id from patent_fact_table,time_year_and_month,organisation ' \
        #        'where patent_fact_table.timekey = time_year_and_month.timekey and ' \
        #        '      patent_fact_table.org_key = organisation.org_id and' \
        #        "      organisation.org_name = '" + company2 + "'and" \
        #        '      time_year_and_month.year_of_time = ' + year
        # data1 = cursor.execute(sql1)
        # data2 = cursor.execute(sql2)

        # return data1,data2

    # 查询某两家公司处于某阶段的专利数量(可用)
    def count_patent_of_two_company_in_a_certain_stage(cursor, company1, company2, stage):
        sql1 = 'select patent_fact_table.id from patent_fact_table,stage,organisation ' \
               'where patent_fact_table.arch_stagekey = stage.stagekey and ' \
               '      patent_fact_table.org_key = organisation.org_id and' \
               "      organisation.org_name = '" + company1 + "'and" \
               "      stage.stage = '" + stage + "'"
        sql2 = 'select patent_fact_table.id from patent_fact_table,stage,organisation ' \
               'where patent_fact_table.arch_stagekey = stage.stagekey and ' \
               '      patent_fact_table.org_key = organisation.org_id and' \
               "      organisation.org_name = '" + company2 + "'and" \
               "      stage.stage = '" + stage + "'"
        data1 = cursor.execute(sql1)
        data2 = cursor.execute(sql2)
        return data1, data2

    # 查询某两家公司某类别的专利数量(可用)
    def count_patent_of_two_company_of_a_certain_category(cursor, company1, company2, category):
        sql1 = 'select patent_fact_table.id from patent_fact_table,category,organisation ' \
               'where patent_fact_table.arch_categorykey = category.categorykey and ' \
               '      patent_fact_table.org_key = organisation.org_id and' \
               "      organisation.org_name = '" + company1 + "'and" \
               "      category.categorykey = '" + category + "'"
        sql2 = 'select patent_fact_table.id from patent_fact_table,category,organisation ' \
               'where patent_fact_table.arch_categorykey = category.categorykey and ' \
               '      patent_fact_table.org_key = organisation.org_id and' \
               "      organisation.org_name = '" + company2 + "'and" \
               "      category.categorykey = '" + category + "'"
        data1 = cursor.execute(sql1)
        data2 = cursor.execute(sql2)

        return data1, data2

    # 查询某两家公司某年的项目数量(可用)
    def count_project_of_two_company_of_a_certain_year(cursor, company1, company2, year):
        sql1 = 'select project_fact_table.id from project_fact_table,time_year,organisation ' \
               'where project_fact_table.project_timekey = time_year.timekey and ' \
               '      project_fact_table.org_key = organisation.org_id and' \
               "      organisation.org_name = '" + company1 + "' and" \
               "      time_year.year = " + year
        sql2 = 'select project_fact_table.id from project_fact_table,time_year,organisation ' \
               'where project_fact_table.project_timekey = time_year.timekey and ' \
               '      project_fact_table.org_key = organisation.org_id and' \
               "      organisation.org_name = '" + company2 + "' and" \
               "      time_year.year = " + year
        data1 = cursor.execute(sql1)
        data2 = cursor.execute(sql2)
        return data1,data2

    # 查询某两家公司某年的项目收益
    def count_project_income_of_two_company_of_a_certain_year(cursor, company1, company2, year):
        sql1 = 'select sum(listed_project_fact_table.income) from listed_project_fact_table,time_year,organisation ' \
               'where listed_project_fact_table.listed_project_timekey = time_year.timekey and' \
               '      listed_project_fact_table.org_id = organisation.org_id and' \
               "      organisation.org_name = '" + company1 + "'and" \
               "      time_year.year = " + year
        sql2 = 'select sum(listed_project_fact_table.income) from listed_project_fact_table,time_year,organisation ' \
               'where listed_project_fact_table.listed_project_timekey = time_year.timekey and' \
               '      listed_project_fact_table.org_id = organisation.org_id and' \
               "      organisation.org_name = '" + company2 + "'and" \
               "      time_year.year = " + year

        cursor.execute(sql1)
        data1 = cursor.fetchone()[0]

        if data1 is None:
            data1 = 0
        else:
            data1 = int(data1)

        cursor.execute(sql2)
        data2 = cursor.fetchone()[0]
        if data2 is None:
            data2 = 0
        else:
            data2 = int(data2)

        return data1, data2

    # 查询某两家公司某类别的项目数量(可用)
    def count_project_of_two_company_of_a_certain_category(cursor, company1, company2, category):
        sql1 = 'select project_fact_table.id from project_fact_table,category,organisation ' \
               'where project_fact_table.project_categorykey = category.categorykey and ' \
               '      project_fact_table.org_key = organisation.org_id and' \
               "      organisation.org_name = '" + company1 + "'and" \
               "      category.category = '" + category + "'"
        sql2 = 'select project_fact_table.id from project_fact_table,category,organisation ' \
               'where project_fact_table.project_categorykey = category.categorykey and ' \
               '      project_fact_table.org_key = organisation.org_id and' \
               "      organisation.org_name = '" + company2 + "'and" \
               "      category.category = '" + category + "'"

        data1 = cursor.execute(sql1)
        data2 = cursor.execute(sql2)

        return data1, data2

    # 查询某两家公司某区域(具体到省)的项目数量
    def count_project_of_two_company_of_a_certain_province(cursor, company1, company2, province):
        sql1 = 'select project_fact_table.id from project_fact_table,project_region,organisation ' \
               'where project_fact_table.project_categorykey = project_region.project_regionkey and ' \
               '      project_fact_table.org_key = organisation.org_id and' \
               "      organisation.org_name = '" + company1 + "'and" \
                "      project_region.province = '" + province + "'"
        sql2 = 'select project_fact_table.id from project_fact_table,project_region,organisation ' \
               'where project_fact_table.project_categorykey = project_region.project_regionkey and ' \
               '      project_fact_table.org_key = organisation.org_id and' \
               "      organisation.org_name = '" + company2 + "'and" \
               "      project_region.province = '" + province + "'"

        data1 = cursor.execute(sql1)
        data2 = cursor.execute(sql2)

        return data1, data2

    # 查询某两家公司某区域(具体到市)的项目数量
    def count_project_of_two_company_of_a_certain_province(cursor, company1, company2, province, city):
        sql1 = 'select project_fact_table.id from project_fact_table,project_region,organisation ' \
               'where project_fact_table.project_categorykey = project_region.project_regionkey and ' \
               '      project_fact_table.org_key = organisation.org_id and' \
               "      organisation.org_name = '" + company1 + "'and" \
               "      project_region.province = '" + province + "'and" \
               "      project_region.city = '" + city + "'"
        sql2 = 'select project_fact_table.id from project_fact_table,project_region,organisation ' \
               'where project_fact_table.project_categorykey = project_region.project_regionkey and ' \
               '      project_fact_table.org_key = organisation.org_id and' \
               "      organisation.org_name = '" + company2 + "'and" \
               "      project_region.province = '" + province + "'and" \
               "      project_region.city = '" + city + "'"

        data1 = cursor.execute(sql1)
        data2 = cursor.execute(sql2)

        return data1, data2

    # 查询某两家公司在某区域的项目支持资金的数额
    def num_of_sp_capital_scale_of_two_company_in_a_certain_region(cursor, company1, company2, province):
        sql1 = 'select sum(sp_capital_scale_fact_table.sp_capital_scale_num) from sp_capital_scale_fact_table,project,project_region,project_id,organisation ' \
               'where sp_capital_scale_fact_table.project_key = project_id.project_key and' \
               '      project_id.project_id = project.project_id and ' \
               '      sp_capital_scale_fact_table.project_regionkey = project_region.project_regionkey and' \
               '      project_id.sp_org_id = organisation.org_id and' \
               "      organisation.org_name = '" + company1 + "'and" \
               "      project_region.province = '" + province + "'"
        sql2 = 'select sum(sp_capital_scale_fact_table.sp_capital_scale_num) from sp_capital_scale_fact_table,project,project_region,project_id,organisation ' \
               'where sp_capital_scale_fact_table.project_key = project_id.project_key and' \
               '      project_id.project_id = project.project_id and ' \
               '      sp_capital_scale_fact_table.project_regionkey = project_region.project_regionkey and' \
               '      project_id.sp_org_id = organisation.org_id and' \
               "      organisation.org_name = '" + company2 + "'and" \
               "      project_region.province = '" + province + "'"

        cursor.execute(sql1)
        data1 = cursor.fetchone()
        cursor.execute(sql2)
        data2 = cursor.fetchone()
        if data1[0] == None:
            data1 = 0
        else:
            data1 = data1[0]
        if data2[0] == None:
            data2 = 0
        else:
            data2 = data2[0]
        return data1, data2

    # 查询某两家公司在某年的项目支持资金的数额
    def num_of_sp_capital_scale_of_two_company_in_a_certain_year(cursor, company1, company2, year):
        sql1 = 'select sum(sp_capital_scale_fact_table.sp_capital_scale_num) from sp_capital_scale_fact_table,project,time_year,project_id,organisation ' \
               'where sp_capital_scale_fact_table.sp_capital_scale_timekey = time_year.timekey and' \
               '      sp_capital_scale_fact_table.project_key = project_id.project_key and' \
               '      project_id.project_id = project.project_id and ' \
               '      project_id.sp_org_id = organisation.org_id and' \
               "      organisation.org_name = '" + company1 + "'and" \
               "      time_year.year = " + year
        sql2 = 'select sum(sp_capital_scale_fact_table.sp_capital_scale_num) from sp_capital_scale_fact_table,project,time_year,project_id,organisation ' \
               'where sp_capital_scale_fact_table.sp_capital_scale_timekey = time_year.timekey and' \
               '      sp_capital_scale_fact_table.project_key = project_id.project_key and' \
               '      project_id.project_id = project.project_id and ' \
               '      project_id.sp_org_id = organisation.org_id and' \
               "      organisation.org_name = '" + company2 + "'and" \
               "      time_year.year = " + year

        cursor.execute(sql1)
        data1 = cursor.fetchone()
        cursor.execute(sql2)
        data2 = cursor.fetchone()
        if data1[0] == None:
            data1 = 0
        else:
            data1 = data1[0]
        if data2[0] == None:
            data2 = 0
        else:
            data2 = data2[0]
        return data1, data2

    # 查询某两家公司在某项目类别的项目支持资金的数额
    def num_of_sp_capital_scale_of_two_company_in_a_certain_category(cursor, company1, company2, category):
        sql1 = 'select sum(sp_capital_scale_fact_table.sp_capital_scale_num) from sp_capital_scale_fact_table,project,category,project_id,organisation ' \
               'where sp_capital_scale_fact_table.project_categorykey = category.categorykey and' \
               '      sp_capital_scale_fact_table.project_key = project_id.project_key and' \
               '      project_id.project_id = project.project_id and ' \
               '      project_id.sp_org_id = organisation.org_id and' \
               "      organisation.org_name = '" + company1 + "'and" \
               "      category.categorykey = '" + category + "'"
        sql2 = 'select sum(sp_capital_scale_fact_table.sp_capital_scale_num) from sp_capital_scale_fact_table,project,category,project_id,organisation ' \
               'where sp_capital_scale_fact_table.project_categorykey = category.categorykey and' \
               '      sp_capital_scale_fact_table.project_key = project_id.project_key and' \
               '      project_id.project_id = project.project_id and ' \
               '      project_id.sp_org_id = organisation.org_id and' \
               "      organisation.org_name = '" + company2 + "'and" \
               "      category.categorykey = '" + category + "'"
        cursor.execute(sql1)
        data1 = cursor.fetchone()
        cursor.execute(sql2)
        data2 = cursor.fetchone()
        if data1[0] == None:
            data1 = 0
        else:
            data1 = data1[0]
        if data2[0] == None:
            data2 = 0
        else:
            data2 = data2[0]
        return data1, data2

    # 获取某两家公司的具体信息
    def get_list(request):
        if request.method == "GET":
            company1 = request.GET.get('company1')
            company2 = request.GET.get('company2')
        if request.method == "POST":
            company1 = request.POST.get('company1')
            company2 = request.POST.get('company2')
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='bi',
                             charset='utf8')

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        sql1 = "select org_categoryid,org_country_name,address,main_product,english_name,employee_number,company_type,g2m_type,legal_rep,business_scope,DATE_FORMAT(establishment_date,'%Y-%m-%d'),url,cooperation,history,profiles,leaders from company where" \
               " org_name = '" + company1 + "'"
        sql2 = "select org_categoryid,org_country_name,address,main_product,english_name,employee_number,company_type,g2m_type,legal_rep,business_scope,DATE_FORMAT(establishment_date,'%Y-%m-%d'),url,cooperation,history,profiles,leaders from company where" \
               " org_name = '" + company2 + "'"

        cursor.execute(sql1)
        data1 = cursor.fetchone()
        cursor.execute(sql2)
        data2 = cursor.fetchone()

        Data1 = {'company1': {'company': company1,'org_categoryid': data1[0], 'org_country_name': data1[1], 'address': data1[2],
                              'main_product': data1[3], 'english_name': data1[4], 'employee_number': data1[5],
                              'company_type': data1[6], 'g2m_type': data1[7], 'legal_rep': data1[8],
                              'business_scope': data1[9], 'establishment_date': data1[10],
                              'url': data1[11],'cooperation': data1[12], 'history': data1[13],
                              'profiles': data1[14], 'leaders': data1[15]}}
        Data2 = {'company2': {'company': company2,'org_categoryid': data2[0], 'org_country_name': data2[1], 'address': data2[2],
                              'main_product': data2[3], 'english_name': data2[4], 'employee_number': data2[5],
                              'company_type': data2[6], 'g2m_type': data2[7], 'legal_rep': data2[8],
                              'business_scope': data2[9], 'establishment_date': data2[10],
                              'url': data2[11],'cooperation': data2[12], 'history': data2[13],
                              'profiles': data2[14],'leaders': data2[15]}}

        Data = {**Data1, **Data2}

        return BaseView.successData(Data)

    def keshihua(request):
        company1 = request.GET.get('company1')
        company2 = request.GET.get('company2')
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='bi',
                             charset='utf8')

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        Data = []
        Data_ = []
        # 测试用
        company1 = '浙江华友钴业股份有限公司'
        company2 = '惠州比亚迪电池有限公司'
        year1 = '2020'
        year2 = '2022'
        # month = '7'
        stage = '授权'
        for i in range(2012,2023):
            data1, data2, data3, data4 = keshihua.count_patent_of_two_company_in_a_certain_year(cursor, company1, company2, str(i))
            Data1 = [{'value': data1, 'name': company1}, {'value': data2, 'name': company2}]
            Data = Data + Data1
        data1, data2, data3, data4 = keshihua.count_patent_of_two_company_in_a_certain_year(cursor, company1, company2, year2)
        Data2 = [{'value': data3, 'name': company1}, {'value': data4, 'name': company2}]

        Data_ = Data_ + Data2

        data1, data2 = keshihua.count_project_of_two_company_of_a_certain_year(cursor, company1, company2,year1)
        Data1 = [{'value': data1, 'name': company1}, {'value': data2, 'name': company2}]
        data3, data4 = keshihua.count_project_income_of_two_company_of_a_certain_year(cursor,company1,company2,year1)
        Data2 = [{'value': data3, 'name': company1}, {'value': data4, 'name': company2}]
        data5, data6 = keshihua.num_of_sp_capital_scale_of_two_company_in_a_certain_year(cursor,company1,company2,year1)
        Data3 = [{'value': float(data5), 'name': company1}, {'value': float(data6), 'name': company2}]

        Data = Data_ + Data + Data1 + Data2 + Data3

        # data1, data2 = keshihua.count_patent_of_two_company_in_a_certain_year(cursor,company1,company2,year2)
        # data1, data2 = keshihua.count_patent_of_two_company_in_a_certain_year_and_month(cursor,company1,company2,year1,month)
        # data3, data4 = keshihua.count_patent_of_two_company_in_a_certain_stage(cursor,company1,company2,stage)
        # data5, data6 = keshihua.num_of_sp_capital_scale_of_two_company_in_a_certain_year(cursor,company1,company2,year1)
        # data7, data8 = keshihua.count_project_income_of_two_company_of_a_certain_year(cursor,company1,company2,year1)
        # Data1 = [{'value': str(data1), 'name': company1}, {'value': str(data2), 'name': company2}]
        # Data2 = [{'value': data3, 'name': company1}, {'value': data4, 'name': company2}]
        # Data3 = [{'value': float(data5), 'name': company1}, {'value': float(data6), 'name': company2}]
        # Data4 = [{'value': data7, 'name': company1}, {'value': data8, 'name': company2}]
        # Data1 = str(Data1[0]).replace("'value'", 'value').replace("'name'", 'name').replace('[','').replace(']','')
        # Data2 = [{'value': str(data3), 'name': company1}, {'value': str(data4), 'name': company2}],
        # Data2 = str(Data2[0]).replace("'value'", 'value').replace("'name'", 'name').replace('[','').replace(']','')
        # Data = Data1 + Data2 + Data3 + Data4
        return BaseView.successData(Data)


