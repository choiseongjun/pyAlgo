from _collections import deque

while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break

    island = [list(map(int, input().split())) for _ in range(h)]

    # 상 우상 우 우하 하 좌하 좌 좌상
    # 8방향 탐색을 위해
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(h):
        for j in range(w):
            print(island[i][j],end='')
        print(sep='')

