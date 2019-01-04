#conding=utf-8
from pyspark.sql import SparkSession
import random

spark = SparkSession  \
    .builder \
     .appName("beijikng") \
    .getOrCreate()

housedata = spark.read.format("csv") \
    .option("header","true") \
    .option("sep",";") \
    .load("/Users/backbook/PycharmProjects/pyspark_demo/data/house.csv")
housedata.show()


ranflot = random.random()  #浮点数
housedata.select("square","price") \
    .map(lambda row : (row[0],row[1],ranflot)) \
    .show()


