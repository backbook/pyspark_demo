#coding=utf8
class Animal:
    def eat(self):
        print("eat")
    def run(self):
        print("run")

class Dog(Animal):
    def bark(self):
        print("wang")
    def run(self):
        super().eat()
        Animal.eat(self)





wangcai = Dog()
wangcai.eat()
wangcai.bark()
wangcai.run()

print("你好")



try:
    pass
    # num = int(input("input"))
except ZeroDivisionError:
    print("请输入正确的整数")
except Exception as res:
    print("未知错误 %s"%res)