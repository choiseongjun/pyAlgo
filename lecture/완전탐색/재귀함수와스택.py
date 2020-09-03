def DFS(x):
    if x>0:
        DFS(x-1)
        print(x)   #밑으로 나두면 스택에 먼저 3 2 1 <- 로 쌓이고 팝해서 1 ,2,3이 나옴 좀 더 알아보기


if __name__=="__main__":
    n=int(input())
    DFS(n)