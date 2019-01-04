# class Soldier:
#     def __init__(self,model,name,age,max_bullet):
#         self.gun = Gun(model)
#         self.name = name
#         self.__age = age
#         self.max_bullet = max_bullet
#     def fair(self):
#         self.gun.shoot()
#     def load(self,bullet_num):
#         self.gun.add_bullet(bullet_num)
#     def __str__(self):
#         return ("%s拿着一把%s枪，进行了打猎开,添加了子弹数%s"%(self.name,self.gun.model,self.max_bullet))
#
#
# class Gun:
#     def __init__(self,model):
#         self.model = model
#         self.bullet_count = 0
#     def add_bullet(self,count):
#         self.bullet_count += count
#     def shoot(self):
#         if self.bullet_count <= 0:
#             print("[子弹数量不足]")
#         else:
#             self.bullet_count = self.bullet_count - 1
#
#
# man = Soldier("AK47","李四",28,20)
# man.load(20)
# print(man._Soldier__age)
# man.fair()
# print(man)


import numpy as np
def sum1(N):
    for i in np.arange(N):
        yield i ** 2
y = sum1(10)
print(type(y))
next(y)
next(y)
next(y)
for i in y:
    print(i)


def add():
    s =1
    b =2
    return s,b
a , b = add()
print(a,b)

