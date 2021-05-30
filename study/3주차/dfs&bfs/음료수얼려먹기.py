
n,m=map(int,input().split())

graph = []
#directions = [(1,0), (-1,0), (0,1), (0,-1)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(int,input())))


def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y]==0:
        graph[x][y]=1

        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        # dfs(x - 1, y)
        # dfs(x, y - 1)
        # dfs(x + 1, y)
        # dfs(x, y + 1)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            dfs(nx,ny)

        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1

print(result)

# 4 5
# 00110
# 00011
# 11111
# 00000