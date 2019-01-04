#coding=utf-8
import logging  # 引入logging模块
# 将信息打印到控制台上
logging.info(u"w")
logging.error(u"11")

try:
    i = 1/0
except ZeroDivisionError as e:
    logging.error(e)
finally:
    print("i know")


