L=int(input)
li=list(map(int,input().split()))
m=input()
li.sort()
for _ in range(m):
    li[0]+=1
    li[L-1]-=1
    li.sort()

print(li[L-1]-li[0])