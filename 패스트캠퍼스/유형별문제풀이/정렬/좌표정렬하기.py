n= int(input())
arr=[]
for _ in range(n):
    x,y = map(int,input().split(' '))
    arr.append((x,y))

arr= sorted(arr)
a = sorted(arr)

for i in a:
   print(i[0],i[1])
# 5
# 3 4
# 1 1
# 1 -1
# 2 2
# 3 3