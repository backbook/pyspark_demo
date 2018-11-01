#!/usr/bin/python
#coding=utf-8

import pymysql


from pyspark.sql import SparkSession
# import numpy as np
# from pyspark.mllib.linalg import Vectors
from pyspark.mllib.stat import Statistics


spark = SparkSession  \
    .builder \
     .appName("beijikng") \
    .getOrCreate()

beijingRdd = spark.sparkContext.textFile("file:///Users/backbook/data/Ml/beijing2.txt")

flatRDD = beijingRdd.flatMap(lambda line : line.split(","))

yearRDD= flatRDD.filter(lambda value : float(value) > 1000)

precipitationRDD = flatRDD.filter(lambda value : float(value) < 1000)

# yearRDD.foreach(print)
# precipitationRDD.foreach(print)
#皮尔逊相关系数验证
PearsonBeijngStat = Statistics.corr(yearRDD,precipitationRDD)
print(PearsonBeijngStat)

# 创建连接
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='Server2008!', db='spark', charset='utf8mb4')
print(conn)

# 创建游标(查询数据返回为元组格式)
# cursor = conn.cursor()

# 创建游标(查询数据返回为字典格式)
cursor = conn.cursor(pymysql.cursors.DictCursor)

# 1. 执行SQL,返回受影响的行数
effect_row1 = cursor.execute("select * from day_video_city_access_topn_stat")

#获取第一行的数据
row_1 = cursor.fetchone()

#获取前n行的数据
row_2 = cursor.fetchmany(3)

row_3 = cursor.fetchall()

print(effect_row1)

print(row_1)
print(row_2)
print(row_3)