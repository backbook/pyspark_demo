#格式化输出

# name = input("请输入名字:")
# age  = input("请输入年龄:")
# msg = "您输入的名字是:%s，今年:%s岁"%(name,age)
# print(msg)


# username = "taibai"
# password = '123'
# i =0
# while i < 3:
#     name = input("请输入你的姓名：")
#     pwd = input("请输入你的密码：")
#     if username == name and password == pwd:
#         print('您登陆成功')
#         break;
#     else:
#         print("登陆失败，你还有%d次登陆机会"%(2-i))
#         if(2-i):
#             result = input('是否再试试')
#             if result == 'yes':
#                 i = 0
#                 continue
#     i += 1
# else:
#     print("选择了不登录")


a = 10
b = 20
print(id(a),id(b))
a,b = b,a
print(id(a),id(b))
print(a,b)

import dis

def func(a,b):
    a, b = b, a
    print(a, b)

a = 10
b = 20


dis.dis(func)

list1 = [1,2,3,4,5,6]
print(id(list1))
list1.append("new")
print(id(list1))
list1.pop()
print(id(list1))
list1[0]="sda"
print(id(list1))
list1=[1,3,4,5,6]
print(id(list1))