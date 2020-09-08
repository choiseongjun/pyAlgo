def hashard(n):
    sum=0
    answer=False
    tmp=n
    while n>0:
        sum+=n%10
        n//=10


    if tmp%sum==0:
        answer=True
    print(answer)
    return answer


n=11
hashard(n)