#!/usr/bin/python
#coding=utf-8


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