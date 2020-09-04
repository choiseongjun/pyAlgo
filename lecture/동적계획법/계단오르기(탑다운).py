def DFS(n):

    if d[n]>0:
        return d[n]
    if n==1 or n==2 or n==3:
        return n
    else:
        d[n]=DFS(n-1)+DFS(n-2)
        return d[n]

n=int(input())
d=[0]*(n+1)
print(DFS(n))
