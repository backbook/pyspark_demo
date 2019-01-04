#coding=utf8
#可以进行读取的python的file数据，默认读取全部内容
# file = open("/Users/backbook/PycharmProjects/pyspark_demo/data/file_test.txt")
# read= file.read()
# print(len(read))
# print("-" * 50)
# read= file.read()
# print(len(read))
# file.close()

#打开文件 写入文件



# file_data = open("/Users/backbook/PycharmProjects/pyspark_demo/data/file_test.txt","a")
# file_data.writelines("hello")
#
# file_data.close()



file = open("/Users/backbook/PycharmProjects/pyspark_demo/data/file_test.txt")

while True:
    text =file.readline()
    if not text:
        break
    print(text,end="")

file.close()
