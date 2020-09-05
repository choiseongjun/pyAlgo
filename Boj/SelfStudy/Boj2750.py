def bubble_sort(arr):
    length=len(arr)-1
    for i in range(length):
        for j in range(length-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)

n=int(input())

li=[]
for i in range(n):
    res=int(input())
    li.append(res)

bubble_sort(li)

