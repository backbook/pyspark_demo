#conding=utf-8


f = open("/Users/backbook/PycharmProjects/pyspark_demo/data/file_test.txt",'r',encoding='utf-8')
try:
    with f as fs:
           for line in f.readlines():
               print(line)
except:
    print("文件位置不存在")
    IOError
finally:
    f.close()

def demo():
    """this is demo"""
    print("this is demo")


# with f as fs:
#     while True:
#      line = f.readline()
#      if not line:break
#      print(line)
# 这种做法是在一个文件数量较少的情况