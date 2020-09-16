import sys

n=int(sys.stdin.readline())
cnt=0
def factorial(n):
    if n<2:
        return 1
    return n*factorial(n-1)

num=factorial(n)
for i in str(num)[::-1]:
    if i=='0':
        cnt+=1
    else:
        break

print(cnt)