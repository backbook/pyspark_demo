#!/usr/bin/python
#coding=utf-8

from pyspark.sql import SparkSession
import numpy as np
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.stat import Statistics


spark = SparkSession  \
    .builder \
     .appName("beijikng") \
    .getOrCreate()

beijingRdd = spark.sparkContext.textFile("file:///Users/backbook/data/Ml/beijing.txt")

statRDD = beijingRdd.flatMap(lambda line: line.split(",")) \
    .map(lambda num: Vectors.dense(np.array([num])))

stats = Statistics.colStats(statRDD)

print(stats.mean())

print(stats.variance())
print(stats.max())

# statRDD.foreach(print)
