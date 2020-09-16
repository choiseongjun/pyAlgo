from math import gcd

def lcm(a,b):
    return a*b//gcd(a,b)
n=int(input())


for i in range(n):
    a,b=map(int,input().split())
    print(lcm(a,b))