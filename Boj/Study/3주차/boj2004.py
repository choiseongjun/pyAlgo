def fac(n):
    global  num
    for i in range(1, n + 1):
        num = num * i
    return num


a,b=map(int,input().split())
num=1
cnt=1

res = (fac(a)//fac(b))//fac(a-b)

for i in str(res)[::-1]:
    if i=='0':
        cnt+=1
    else:
        break
print(cnt)