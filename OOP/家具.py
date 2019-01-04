class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return "[%s] 占地 %.2f"%(self.name,self.area)


class House:
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []
    def __str__(self):
        #Python能够自动的将括号内部的代码连接一块
        return ("户型： %s\n总面积： %.2f[剩余：%.2f]\n家具： %s"
                %(self.house_type,self.area,
                  self.free_area,self.item_list))
    def add_item(self,item):
        print("要添加的家具%s" % item)
        if item.area > self.free_area/6:
            print("%s 家具面积大于房子的剩余面积 %s"%(item.area,self.free_area))
            print("请查看是否出错了")
        else:
            self.free_area = self.free_area - item.area
            self.item_list.append(item.name)





bed = HouseItem("席梦思",4)
chest = HouseItem("衣柜",200)
table = HouseItem("餐桌",1.5)
print(chest)
print(bed)
print(table)


#创建房子的对象
my_home = House("两室一厅",120)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)