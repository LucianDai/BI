import csv
import py2neo
from py2neo import Graph,Node,Relationship,NodeMatcher

g=Graph('http://localhost:7474/',user='neo4j',password='123456789',name='neo4j')

with open('C:/Users/linda/Desktop/企业行业竞争对手主题分析系统/产业链CSV表utf-8/xinnengyuan.csv','r',encoding='utf-8') as f:
    reader = csv.reader(x.replace('\0', '') for x in f)
    for item in reader:
        if reader.line_num==1:
            continue
        print("当前行数:",reader.line_num,"当前内容:",item)
        start_node=Node("Product",name=item[0])
        end_node=Node("Product",name=item[1])
        relation=Relationship(start_node,item[3],end_node)
        #g.create(start_node)
        #g.create(end_node)
        #g.create(relation)
        g.merge(start_node,"Product","name")
        g.merge(end_node,"Product","name")
        g.merge(relation,"Product","name")

    with open('C:/Users/linda/Desktop/企业行业竞争对手主题分析系统/产业链CSV表utf-8/zhongduanbujian.csv', 'r',
              encoding='utf-8') as f:
        reader = csv.reader(x.replace('\0', '') for x in f)
        for item in reader:
            if reader.line_num == 1:
                continue
            print("当前行数:", reader.line_num, "当前内容:", item)
            start_node = Node("Product", name=item[0])
            end_node = Node("Terminal", name=item[1])
            relation = Relationship(start_node, item[3], end_node)
            # g.create(start_node)
            # g.create(end_node)
            # g.create(relation)
            g.merge(start_node, "Product", "name")
            g.merge(end_node, "Terminal", "name")
            g.merge(relation, "Product", "name")

    with open('C:/Users/linda/Desktop/企业行业竞争对手主题分析系统/产业链CSV表utf-8/peihe.csv', 'r',
              encoding='utf-8') as f:
        reader = csv.reader(x.replace('\0', '') for x in f)
        for item in reader:
            if reader.line_num == 1:
                continue
            print("当前行数:", reader.line_num, "当前内容:", item)
            start_node = Node("Terminal", name=item[0])
            end_node = Node("Terminal", name=item[1])
            relation = Relationship(start_node, item[3], end_node)
            # g.create(start_node)
            # g.create(end_node)
            # g.create(relation)
            g.merge(start_node, "Terminal", "name")
            g.merge(end_node, "Terminal", "name")
            g.merge(relation, "Terminal", "name")

    with open('C:/Users/linda/Desktop/企业行业竞争对手主题分析系统/产业链CSV表utf-8/gongsi-product.csv', 'r',
              encoding='utf-8') as f:
        reader = csv.reader(x.replace('\0', '') for x in f)
        for item in reader:
            if reader.line_num == 1:
                continue
            print("当前行数:", reader.line_num, "当前内容:", item)
            start_node = Node("Corporation", name=item[0], product=item[3])
            end_node = Node("Product", name=item[1], )
            relation = Relationship(start_node, item[2], end_node)
            # g.create(start_node)
            # g.create(end_node)
            # g.create(relation)
            g.merge(start_node, "Corporation", "name")
            g.merge(end_node, "Product", "name")
            g.merge(relation, "Corporation", "name")

    with open('C:/Users/linda/Desktop/企业行业竞争对手主题分析系统/产业链CSV表utf-8/gongsi-terminal.csv', 'r',
              encoding='utf-8') as f:
        reader = csv.reader(x.replace('\0', '') for x in f)
        for item in reader:
            if reader.line_num == 1:
                continue
            print("当前行数:", reader.line_num, "当前内容:", item)
            start_node = Node("Corporation", name=item[0], product=item[3])
            end_node = Node("Terminal", name=item[1], )
            relation = Relationship(start_node, item[2], end_node)
            # g.create(start_node)
            # g.create(end_node)
            # g.create(relation)
            g.merge(start_node, "Corporation", "name")
            g.merge(end_node, "Terminal", "name")
            g.merge(relation, "Corporation", "name")

