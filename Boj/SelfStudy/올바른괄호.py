def solution(s):
    answer = True
    cnt=0
    li=[]
    for i in s:
        if i=='(':
            li.append(i)
        elif i==')':
            try:
                li.pop()
            except IndexError:
                return False
    print(li)
    return len(li)==0

s="(()("
print(solution(s))