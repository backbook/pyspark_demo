#!/usr/bin/python
#coding=utf-8

#卡方检验
import numpy as np
from pyspark.mllib.linalg import Vectors,Matrices
from pyspark.mllib.stat import Statistics

#数据的表，将表进行输入
#       男    女
#  左手 127   147
#  右手 19    10
##要论证的一个东西是：论证假设，左右手是否是具有相关性的
##主要是统计学中，可以确定我们的常规的发生条件，比如医疗中药物的计算

data = Matrices.dense(2,2,np.array([127,19,147,10]))

test = Statistics.chiSqTest(data)



print(test)

##比较 0.5
# 大于0.5可以进行检验，可以被接受，否则被推翻
#假设条件