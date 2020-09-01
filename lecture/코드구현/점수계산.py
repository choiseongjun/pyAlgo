# 10
# 1 0 1 1 1 0 0 1 1 0
n=int(input())
li=list(map(int,input().split()))
cnt=0
sum=0
for x in a:
    if x==1:
        cnt+=1
        sum+=cnt
    else:
        cnt=0
print(sum)
# for i in range(n):
#
#     for j in range(0,i+1):
#         if li[j]==1:
#             cnt+=1
#
#         elif li[j]==0:
#             cnt=0
#
#     sum+=cnt
#
# print(sum)






