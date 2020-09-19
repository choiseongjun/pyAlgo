import sys

while True:
    n=int(sys.stdin.readline())
    a = [False, False] + [True] * (n - 1)
    primes=[]
    sum = 0
    if n==0:
        break
    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False
    for k in range(len(primes)):
        if primes[k-1]+primes[k]==n:
            print(n,"=",primes[k-1],"+",primes[k])

