from collections import deque
def solution(s):
    answer = 0
    dq=deque()
    cnt=0
    for i in s:
        dq.append(i)

    while dq:
        print(dq.popleft())

    print(cnt)
    return answer

s="hbcdcba"
solution(s)