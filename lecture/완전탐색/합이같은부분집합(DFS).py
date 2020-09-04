import sys

#이해 정확히 하고가기

def DFS(L,sum):
    if sum>total//2:
        return
    
    if L==n:
        if sum==(total-sum):
            print("Yes")
            sys.exit(0)
    else:
        DFS(L+1,sum+a[L])
        DFS(L + 1, sum)


if __name__ =="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    total=sum(a)
    DFS(0,0)
    print("NO")

# 6
# 1 3 5 6 7 10