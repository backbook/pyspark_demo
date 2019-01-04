class Cat:
    #最开始的时候对象会进行一个创建空间划定空间
    #初始化方法，类似的是java的对象的构造方法
    def __init__(self,name):
        self.name=name
    #self指的是自己的本身引用
    def eat(self):
        """传入需要的食物菜单

        :param food: 需要吃的食物
        """
        print("%s is like yu"%self.name)
    def drink(self):
        print("%s need water"%self.name)
    #跟java的toString是一样的
    def __str__(self):
        return self.name
    #这个是在最后的市价
    def __del__(self):
        print("%s 我走了"%self.name)
##对象销毁之前会进行del，__del__

tom = Cat("tom")
jack = Cat("jack")

#不推荐适用这种方式
# tom.name = "xiaoxue"
# jack.name = "lazy cat"

tom.eat()
tom.drink()
jack.eat()
jack.drink()


addr = id(tom)
print(addr)
print("cat is",tom)
#类的外部增加属性，不适用

del tom

