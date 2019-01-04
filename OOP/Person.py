
class Person:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    def  __str__(self):
        return "我的名字是 %s 体重是 %.2f"%(self.name,self.weight)
    def run(self):
        pass
    def eat(self):
        pass

xiaoming = Person("小明",19,70.0)
xiaoming.run()
xiaoming.eat()
print(xiaoming)