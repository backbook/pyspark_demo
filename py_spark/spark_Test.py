#coding=utf-8
from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark =  SparkSession.\
        builder.\
        master("local[2]").\
        appName("Sparktest").\
        getOrCreate


    spark.stop()
