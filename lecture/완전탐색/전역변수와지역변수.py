
def DFS1():
    print(cnt)
def DFS2():
    global cnt
    if cnt==5:
        cnt+=1
        print(cnt)

if __name__=="__main__":
    cnt=5
    DFS1()
    DFS2()
    print(cnt)