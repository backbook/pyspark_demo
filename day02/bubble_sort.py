arr = [7,4,3,67,525,23,42]

#第一种写法
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