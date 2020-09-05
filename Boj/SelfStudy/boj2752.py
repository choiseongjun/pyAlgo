a,b,c=map(int,input().split())

li=[]
li.append(a)
li.append(b)
li.append(c)
li.sort(reverse=False)
for i in li:
    print(i,end=' ')