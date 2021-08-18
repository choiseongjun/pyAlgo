# 정점이 좌표의 형태 - 0, 1의 정보 사용
R, C = 7, 8
AM = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 0, 1, 1, 1, 1]]

AM = [[1] + list(map(int,input().split()))+ [1] for _ in range(R)]
AM.insert(0, [1]*(C+2))
AM.append([1]*(C+2))

AM = [list(map(int,input().split())) for _ in range(R)]