def no_continuous(s):
    answer=[]
    for i,v in enumerate(s):
        if i==0:
            answer.append(v)
        elif s[i-1]==v:
            continue
        else:
            answer.append(v)
        print(answer)



s='133303'
no_continuous(s)