n=int(input())
li=list(map(int,input().split()))
avg=round(sum(li)/n)
min=2147000000

for idx,x in enumerate(li):
    tmp=abs(x-avg)#거리구하기
    if tmp<min:
        min=tmp
        score=x#점수
        res=idx+1#학생번호
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1
print(avg,res)

#round_half_up


# for i in range(n):
#     sum+=li[i]
#     avg=sum/n
#     print(li.sort())
#     if (i==n-1):
#         print(avg)
#         if li[i]<=avg or avg<=li[i]:
#             print("")

