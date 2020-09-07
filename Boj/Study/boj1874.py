n=int(input())

stack=[]
answer=[]
count=1
temp=True
for i in range(n):
    a=int(input())
    i=0
    while count<=a:
        stack.append(count)
        count+=1
        answer.append('+')
    if stack[-1]==n:
        stack.pop()
        answer.append('-')
    else:
        temp=False
if temp==False:
    print("No")
else:
    print()

