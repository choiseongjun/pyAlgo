n=int(input())
li=list(map(int,input().split()))
cnt=0
def isPrime(x):
    global cnt
    if x<2:
        return False
    else:
        for i in range(2,x):
            if x%i == 0:
                return False
        return True

for i in range(len(li)):

    res = isPrime(li[i])
    if res==True:
        cnt+=1

print(cnt)
