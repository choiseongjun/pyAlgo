from _collections import deque
n,k=map(int,input().split())
dq=[(pos,val) for pos,val in enumerate(list(map(int,input().split())))]
dq=deque(dq)
cnt=0
while dq:
    cur=dq.popleft()

    if any(cur[1]<x[1] for x in dq):
        dq.append(cur)
    else:
        cnt+=1
        if cur[0]==k:
            break


print(cnt)

# 5 2
# 60 50 70 80 90