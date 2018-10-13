from __future__ import print_function

from pyspark.sql import SparkSession
import logging
logging.basicConfig(level = logging.INFO)

if __name__ == "__main__":
    """
        Usage: pi [partitions]
    """
    spark = SparkSession\
        .builder\
        .appName("PythonPi")\
        .getOrCreate()
    spark.sparkContext.setLogLevel("WARN")
    text_file = spark.sparkContext.textFile("/data/test.txt")
    counts = text_file.flatMap(lambda line: line.split(".")) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a + b)
    arr = counts.collect()
    for i in arr:
        print(i)