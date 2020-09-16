n=int(input())
li=list(map(int,input().split()))
stk=[]
res=[-1 for _ in range(n)]

for i in range(len(li)):

    try:
        while li[stk[-1]]<li.count(i):
            res[stk.pop()]=li[i]
    except:
        pass
    stk.append(li.count(i))

for i in range(n):
    print(res[i],end=' ')