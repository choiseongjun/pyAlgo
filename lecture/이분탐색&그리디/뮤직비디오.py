k,n=map(int,input().split())

res=0
largest=0
li=list(map(int,input().split()))
lt=1
rt=sum(li)
def Count(capacity):
    cnt=1
    sum=0
    for x in li:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

for i in range(len(li)):
    rt+=li[i]

maxx=max(li)
cnt=0
res=0
while lt<rt:
    mid=(lt+rt)//2
    if mid>maxx and Count(mid)<=n:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)
    # if cnt==n:
    #     res=mid
    #     break
    # elif cnt<n:






# 9 3
# 1 2 3 4 5 6 7 8 9