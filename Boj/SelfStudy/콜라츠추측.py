def solution(num):
    cnt=0
    while num>1:
       num=num*3+1 if num%2 else num/2
       cnt+=1
    print(cnt)
    return cnt

num=626331
solution(num)