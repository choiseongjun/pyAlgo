MAX = 1000000
prime = [False for _ in range(MAX+1)]
prime[1] = True

for i in range(2, MAX+1):
    if i*i > MAX:
        break
    if prime[i] is False:
        for j in range(i*i, MAX+1, i):
            prime[j] = True

m, n = map(int, input().split())
for i in range(m, n+1):
    if prime[i] is False:
        print(i)
