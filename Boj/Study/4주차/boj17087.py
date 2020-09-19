n,m=map(int,input().split())
t=list(map(int,input().split()))
cnt=0
res=0
res1=0

for i in range(len(t)):
    if m<t[i]:
        m+=1
        cnt+=1
        if m==t[i]:
            break
    if m>t[i]:
        m-=1
        cnt+=1
        if m==t[i]:
            break
    print(cnt)

    # for i in range(len(t)):
    #     if m>t[i]:
    #         m-=1
    #         cnt+=1
    #         res=cnt
    #         if m==t[i]:
    #             break
    #     elif m<t[i]:
    #         m+=1
    #         cnt+=1
    #         res1=cnt
    #         print(res1)
    #         if m==t[i]:
    #             break

