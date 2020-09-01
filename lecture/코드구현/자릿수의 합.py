def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x//=10
    return sum



n=int(input())
a=list(map(int,input().split()))
max=-2147000000
# for i in range(n):
for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x
print(res)

#test
# 3
# 125 15232 97
