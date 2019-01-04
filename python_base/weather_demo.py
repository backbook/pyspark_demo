#coding=utf-8

import random
from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager


#设置字体
my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

#windows、linux设置字体
# font = {'family' : 'Microsoft Yahei',
#        'weight' : 'bold',
#        'size' : 'larger'}
# matplotlib.rc("font",**font)
x =  range(0,120)
y = [random.randint(20,35) for i in range(120)]

plt.figure(figsize=(15,15),dpi = 80)
plt.plot(x,y)

_x = list(x)

# plt.xticks(x)

_x_lables = ["10点{}分".format(i) for i in range(60)]
_x_lables  +=  ["11点{}分".format(i) for i in range(60)]

plt.xticks(_x[::3],_x_lables[::3],rotation=45,fontproperties=my_font)

plt.yticks(y)

plt.show()

try:
    1+2
except Exception:
    print()