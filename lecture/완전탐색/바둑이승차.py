from _collections import deque
#복습
def DFS(L,sum,tsum):
    global result
    global total
    if sum+(total-tsum)<result:
        return
    if sum>c:
        return
    if L==n:
        if sum>result:
            result=sum
    else:
        DFS(L+1,sum+a[L],tsum+a[L])
        DFS(L+1,sum,tsum+a[L])

if __name__=="__main__":
    c,n=map(int,input().split())
    a=[0]*n
    result=-2147000000
    for i in range(n):
        a[i]=int(input())
    total=sum(a)
    DFS(0,0,0)
    print(result)

# 259 5
# 81
# 58
# 42
# 33
# 61