n,limit=map(int,input().split())
p=list(map(int,input().split()))
cnt=0
p.sort()

while p:
    if len(p)==1:
        cnt+=1
        break
    if p[0]+p[-1]>limit:
        p.pop()#가장무거운사람만 나감
        cnt+=1
    else:
        p.pop(0)
        p.pop()
        cnt+=1

print(cnt)
# 5 140
# 90 50 70 100 60