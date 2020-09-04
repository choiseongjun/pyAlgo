def bubbleSort_ASC(arr):
    n=len(arr)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def bubbleSort2_Asc(arr):
    n = len(arr)
    for i in range(n-1,-1,-1):
        change=False
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                change=True
            if change==False:
                break
    return arr


def bubbleSort_Desc(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1,i,-1):
            if arr[j]>arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
    return arr



arr=[6, 5, 1, 4, 7, 2, 3]
a=bubbleSort_ASC(arr)
print(a)
b=bubbleSort_Desc(arr)
print(b)
c=bubbleSort2_Asc(arr)
print(c)