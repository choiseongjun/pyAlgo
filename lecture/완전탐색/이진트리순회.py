def DFS(v):
    if v>7:
        return
    else:
        print(v)
        DFS(v*2)#왼쪽자식
        DFS(v*2+1)#오른쪽자

if __name__=="__main__":
    DFS(1)