
def DFS(L):
    global cnt
    if L==m:
        for j in range(m):
            print(res[j],end=' ')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            res[L]=i;
            DFS(L+1)

if __name__=="__main__":
    n,m=map(int,input().split())
    res=[0]*n
    cnt=0
    DFS(0)
    print(cnt)

# res[0]=1,2,3
# res[1]=1,2,3