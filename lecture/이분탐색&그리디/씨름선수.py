n=int(input())
body=[]
for i in range(n):
    a,b=map(int,input().split())
    body.append(a,b)
body.sort(reverse=True)
largest=0
cnt=0
for x,y in body:
    if y>largest:
        largest=y
        cnt+=1

print(cnt)


# 5
# 172 67
# 183 65
# 180 70
# 170 72
# 181 60

# n=int(input())
# res=[]
# ##이 문제는 키는 고려할필요가없음 순차적으로 정렬되어있기떄문에 그래서 아래문제서 키를 뺴면됨
# for i in range(n):
#     s,e=map(int,input().split())
#     res.append((s,e))
#
# res.sort(reverse=True,key=lambda x:(x[0],x[1]))
# et=0
# st=0
# cnt=0
# for s,e in res:
#     if e>et or s>st:
#         et=e
#         st=s
#         cnt+=1
#
# print(cnt)

