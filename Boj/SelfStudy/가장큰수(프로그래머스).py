##아래코드는 틀림 
def solution(numbers):
    answer = ''
    res=[]
    for i in numbers:
        answer+=str(i)

    res.append(answer)
    i=int(answer)

    answer = "".join(sorted(str(answer),reverse=True))
    print(answer)
    return answer

numbers=[3, 30, 34, 5, 9]
solution(numbers)