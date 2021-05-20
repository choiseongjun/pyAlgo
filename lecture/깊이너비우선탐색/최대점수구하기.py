def DFS(L,sum,time):
    global res
    if time>m:
        return
    if L==n:
        if sum>res:
            res=sum
    else:
        DFS(L+1,sum+pv[L],time+pt[L])
        DFS(L+1,sum,time)


if __name__=="__main__":
    n,m=map(int,input().split())
    pv=list()#최대점수
    pt=list()#제한시간
    for i in range(n):
        a,b=map(int,input().split())
        pv.append(a)
        pt.append(b)
    res=-2147000000
    DFS(0,0,0)
    print(res)

# 5 20
# 10 5
# 25 12
# 15 8
# 6  3
# 7  4