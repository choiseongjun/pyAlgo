from _collections import deque
#이문제는 k번 계쏙 돌아서 팝을 하고 다시 어팬드해서 3번씩 반복해가지고 마지막 남은 수를 출력한다
n,k=map(int,input().split())
dq=list(range(1,n+1))
dq=deque(dq)
while dq:#큐가 빌떄까지
    for _ in range(k-1):
        cur=dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        dq.popleft()#마지막 큐까찌 뺴기 때문에 종료됨
#입력
#8 3


# 1 2 3 4 5 6 7 8
# 4 5 6 7 8 1 2
# 6 7 8 1 2 4 5
# 7 8 1 2 4 5
# 1 2 4 5 7 8
# 2 4 5 7 8
# 5 7 8 2 4
# 7 8 2 4
# 2 4 7 8
# 4 7 8
# 8 4 7
# 4 7
# 7 4
# 4 7
# 7