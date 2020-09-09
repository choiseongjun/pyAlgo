# def solution(n): ##테스트케이스 실패
#     answer = 0
#     dp=[0]*(n+1)
#     dp[0]=0
#     dp[1]=1
#     dp[2]=2
#     dp[3]=3
#     for i in range(4,n+1):
#         dp[i]=dp[i-1]+dp[i-2]
#         #dp[4]=dp[3]+dp[2]
#         #dp[3]=dp[2]+dp[1]
#         #dp[2]=dp[1]+dp[0]
#     answer=dp[n]
#     return answer%1234567
# def solution(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 2
#
#     answer=solution(n-1)+solution(n-2)
#     return answer
#solution(3)+solution(2)  +2+1
# def solution(n):
#     answer=0
#     lst=[0 for i in range(n+1)]
#     lst[0]=1
#     lst[1]=2
#     for i in range(2,n+1):
#         lst[i]=lst[i-1]+lst[i-2]%1234567
#     answer=list[n-1]%1234567
#     return answer
n=4
result = solution(n)
print(result)