from collections import deque
n,a=map(int,input().split())
dq = deque()
for i in range(1,n+1):
    dq.append(i)
i=0
stack=[]
while dq:
    for _ in range(a-1):
        cur=dq.popleft()
        dq.append(cur)
    stack.append(dq.popleft())
    if len(dq)==0:
        break



print("<", end='')
for i in stack:
    if i==stack[-1]:
        print(i,end='')
    else:
        print("%s, "%(i),end='')
print(">")