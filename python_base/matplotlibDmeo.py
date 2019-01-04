#coding=utf-8
from matplotlib import pyplot as plt
#这个是为了设置画布大小和画布的锯齿
plt.figure(figsize=(20,8),dpi = 80)
x = range(2,26,2)
y = [15,12.1,4,2,31,42,5,2,32,42,12,23]

#绘图操作
plt.plot(x,y)


#设置轴的刻度
_xticks_lable = [i/2 for i in range(4,49,1)]

plt.xticks(_xticks_lable[::2])

plt.yticks(range(min(y),max(y)+1))
#保存图片的操作
# plt.savefig(".figureDemo_test.png")
#显示
plt.show()

