def solution(s):
    answer = True
    cnt=0
    res=[]
    s.lower().count('p')==s.lower().count('y')
    # for i in s.lower():
    #     if i=='p' or i=='y':
    #         res.append(i)
    #
    # for j in res:
    #     if j=='p':
    #         cnt+=1
    #     elif j=='y':
    #         cnt-=1
    #     if cnt==0:
    #         answer=True
    #     else:
    #         answer=False
    # print(answer)
    return answer

s="Pyy"
solution(s)