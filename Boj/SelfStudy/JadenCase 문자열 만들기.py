def jaden(s):
    answer='"'
    for i in s.split():
        i=i[0].upper()+i[1::].lower()
        answer+=i+" "
        # if i==len(s)-1:
        #     answer+='"'

    print(answer)
    return answer






s="for the last week"
result = jaden(s)
