def DFS(l,sum):
    global res
    if l>res:
        return
    if sum>res:
        return
    if sum==k:
       if l<res:
           res=l
    else:
        for i in range(n):
            DFS(l+1,sum+m[i])

if __name__=='__main__':
    n=int(input())
    m=list(map(int,input().split()))
    k=int(input())
    res=2147000000
    m.sort(reverse=True)
    DFS(0,0)
    print(res)

# 3
# 1 2 5
# 15