from collections import deque

deq = deque()
n,k = map(int,input().split())


for i in range(1,n+1):
    deq.append(i)

while deq:
    for _ in range(k-1):
        cur = deq.popleft()
        deq.append(cur)
    deq.popleft()

    if len(deq)==1:
        print(deq[0])
        break

