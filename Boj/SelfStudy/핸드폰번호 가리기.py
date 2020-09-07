def solution(phone_number):
    print('*' * (len(s) - 4) + s[-4:])
    cnt = 0
    answer = ""
    for i in phone_number:
        cnt += 1
        if cnt>len(phone_number)-4 and cnt<=len(phone_number):
            answer+=i
        else:
            answer+=i.replace(i,"*")
    return answer

s="01033334444"
solution(s)