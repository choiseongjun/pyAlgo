from _collections import deque
itext=input()
n=int(input())
for i in range(n):
    plan=input().split()
    dq=deque(itext)
    for x in plan:
        if x in plan:
            if x!=dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))

# CBA
# 3
# CBDAGE
# FGCDAB
# CTSBDEA