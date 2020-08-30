import sys

N = int(sys.stdin.readline())
stairs = list()
for i in range(N):
    stairs.append(int(sys.stdin.readline()))

dp = list()
dp.append(stairs[0])
dp.append(stairs[1] + stairs[0])
dp.append(max(stairs[1] + stairs[2], stairs[0] + stairs[2]))

for i in range(3, N):
    dp.append(max(stairs[i] + dp[i - 2], stairs[i] + stairs[i - 1] + dp[i - 3]))
print(dp[N - 1])

#start[3]+score[1] , stair[3]+stars[2]+score[0]
#score[0]==10
#score[1]==30
#score[2]==35