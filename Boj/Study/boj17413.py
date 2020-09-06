text=input()
answer=""
tmp=""
check=False
for i in text:
    if i=='<':
        check=True
        answer+=tmp[::-1]+i
        tmp=''
    elif i=='>':
        check=False
        answer+=i
    elif i==' ':
        answer+=tmp[::-1]+i
        tmp=''
    elif check:
        answer+=i
    else:
        tmp+=i

print(answer)

#먼저 <시작될때부터 check로 True False를 걸어준다음 Check를 걸면
#그 <>안에 내용만 따로 출력되고 else는 괄호밖에 출력된다
#elif에 띄워쓰공백을 걸어버린 이유는 문장별로 역순출력하기 위해서 걸었다
#check안에 내용은 <> 사이에 내용이라 i를 그대로 넣어준다



