def minPathSum(grid):

    height=len(grid)
    if height==0:
        return 0
    width=len(grid[0])

    dp=[[0 for _ in range(width)] for _ in range(height)]#0으로 초기화
    for i in range(height-1,-1,-1):#역으로 출력
        for j in range(width-1,-1,-1):
            if i==height-1 and j==width-1:
                dp[i][j]=grid[-1][-1]
                continue
            if i==height-1:
                dp[i][j]==grid[i][j]+dp[i][j+1]
                continue
            if j==width-1:
                dp[i][j]=grid[i][j]+dp[i+1][j]
                print(dp)
                continue

            dp[i][j]=grid[i][j]+min(dp[i][j+1],dp[i+1][j])
    return dp[0][0]


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
minPathSum(grid)