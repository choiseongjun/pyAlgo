def ascending(arr):
    now = arr[0]
    result = 1
    for i in range(1,len(arr)):
        if now<arr[i]:
            result+=1
            now =arr[i]
        return result



n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

a = ascending(arr)
print(a)
a