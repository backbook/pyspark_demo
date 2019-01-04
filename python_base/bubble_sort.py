arr = [7,4,3,67,525,23,42]

#第一种写法
''''
冒泡排序的思想
最开始想到，比如有 arr = [7,4,3,67,525,23,42] 
关注点： 个数据在一个list里面，那么在循环排序的时候，需要n-1，两两互相交换
而在这个关注点上，开始进行使用range(0,n-1) 则这个样式出来的结果为:0,1,2,3,4,.....,n-1-1 次数则是n-1次循环
这一层的映射可以表示为：
0    在这里排序的次数也是将最大的数进行冒出，则第一次需要，n-1比较，次数随着整体进行减少，n-1-j  n-1-0
1    n-1-1
2    n-1-2
3    n-1-3
4    ...
5
6    
...
n-1-1  n-1-(n-1-1)






'''
def bubble_sort_1(arr):
    n = len(arr)
    for j in range(0,n - 1):
        for i in range(0,n-1-j):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]

bubble_sort_1(arr)
print(arr)

def bubble_sort_2(arr):
    for j in range(len(arr)-1,0,-1):
        for i in range(0,j):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]

bubble_sort_2(arr)
print(arr)


#进行优化
def bubble_sort3(arr):
    for j in range(len(arr)-1, 0, -1):
        count = 0
        for i in range(0, j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                count += 1
        if count == 0:
            return
bubble_sort3(arr)
print(arr)