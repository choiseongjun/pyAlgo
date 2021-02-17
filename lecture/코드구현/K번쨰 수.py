

T= int(input())

for i in range(T):
    n,s,e,k = map(int,input().split())
    a=list(map(int,input().split()))
    a = a[s-1:e]
    a.sort()
    for idx,v in enumerate(a):
        print(a[k-1])


