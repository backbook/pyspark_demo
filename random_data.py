#coding=utf-8

from faker import Faker

# fake=Faker() #默认生成美国英文数据
fake=Faker(locale='zh_CN')
#/Users/backbook/data/txt/sudent.data
for i in range(10000):
    data = str(i) + "|" + fake.name() + "|" + fake.phone_number()+ "|" + fake.company() + "|" + fake.address()
    print(data)
    with open("/Users/backbook/data/txt/sudent.data",'a+',encoding='utf-8') as studentFile:
        studentFile.writelines(data+"\n")

studentFile.close()
