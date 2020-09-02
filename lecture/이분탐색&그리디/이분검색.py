n,m=map(int,input().split())
li=list(map(int,input().split()))

lt=0
rt=n-1
li.sort()
print(li)
while lt<=rt:
    mid=(lt+rt)//2
    if li[mid]==m:
        print(mid+1)
        break
    elif li[mid]>m:
        rt=mid-1
    else:
        lt=mid+1
