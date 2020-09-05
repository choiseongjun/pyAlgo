import sys
a=int(sys.stdin.readline())
li=[]

for i in range(a):
    li.append(int(input()))

dp=[]
dp.append(li[0])
dp.append(li[0]+li[1])
dp.append(max(li[2]+li[0],li[2]+li[1]))
for i in range(3,a):
    dp.append(max(dp[i-3]+li[i-1]+li[i],dp[i-2]+li[i]))#마지막경우를 밟는경우 밟지않는경우

print(dp[a-1],end='')