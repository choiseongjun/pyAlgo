S = str(input())
alpabet = [chr(i) for i in range(97,123)]

for i in alpabet:
    try:
        print(S.index(i),end = ' ')
    except:
        print(-1,end=' ')
