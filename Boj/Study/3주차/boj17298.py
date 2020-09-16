numbers = int(input())
li = list(map(int, input().split()))
stk = []
result = [-1 for _ in range(numbers)]

for i in range(len(li)):
    try:
        while li[stk[-1]] < li[i]:
            result[stk.pop()] = li[i]
    except:
        pass

    stk.append(i)

for i in range(numbers):
    print(result[i], end=' ')