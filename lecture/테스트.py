

n = int(input())

a=list(map(int,input().split()))


b=[]
def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x//=10
    return sum


max=-2147000000
for i in a:
    tot=digit_sum(i)
    if tot>max:
        max=tot
        res=i
print(res)
# print(b)

# 3
# 125 15232 97