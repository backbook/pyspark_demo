#!/usr/bin/python
#coding=utf-8

#NaiveBayes 朴素贝叶斯

from pyspark.sql import SparkSession


spark = SparkSession  \
    .builder \
     .appName("beijikng") \
    .getOrCreate()

data = spark.sparkContext.textFile("/Users/backbook/data/Ml/NaiveBayes.txt")

data.foreach(print)
