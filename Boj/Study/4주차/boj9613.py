from itertools import combinations
from sys import stdin
input = stdin.readline

def gcd(a,b):
    if b == 0: # 나머지
        return a # 최대공약수
    return gcd(b,a%b)

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    ans = 0
    for e in list(combinations(arr[1:], 2)):
        ans += gcd(e[0], e[1])
    print(ans)