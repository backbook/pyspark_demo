#!/usr/bin/python
# #coding=utf-8

from faker import Faker
import happybase



import sys

x = "w"
sys.stdout.write(x+'/n')


# connection = happybase.Connection('localhost')
# print(connection.tables())
# table = connection.table('test')
# for key, value in table.scan():
#     print(key,  bytes(value))
# fake=Faker(locale='zh_CN')
#



# bath = table.batch()
# for i in range(100):
#     bath.put("range"+str(i),{'info:id': str(i),'info:name':fake.name(),'info:phone_number':fake.company(),'info:address':fake.address()})
# bath.send()


# fake=Faker() #默认生成美国英文数据
fake=Faker(locale='zh_CN')
#/Users/backbook/data/txt/sudent.data
for i in range(10000):
    data = str(i) + "|" + fake.name() + "|" + fake.phone_number()+ "|" + fake.company() + "|" + fake.address()
    with open("/Users/backbook/data/txt/sudent.data",'a+',encoding='utf-8') as studentFile:
        studentFile.writelines(data+"\n")

studentFile.close()
