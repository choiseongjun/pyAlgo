
N=3
arr = [0]*11


def DFS(depth):
    global N
    global arr
    if depth > N:
        for i in range(1,N+1):
            print(arr[i])
        print(end="\n")
        return
    for i in range(1,7):
        #arr[depth] = i
        arr[depth] = i
        DFS(depth+1)

if __name__ == '__main__':
    DFS(0)
