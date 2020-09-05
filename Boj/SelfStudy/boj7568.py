n=int(input())

li=[]
for i in range(n):
    a,b=map(int,input().split())
    res=(a,b)
    li.append(res)

for i in li:
    rank=1
    for j in li:
        if i[0]<j[0] and i[1]<j[1]:
            rank+=1
    print(rank,end=' ')