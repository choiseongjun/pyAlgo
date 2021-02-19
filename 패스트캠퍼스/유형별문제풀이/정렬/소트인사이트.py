n = int(input())
res = []
answer=""
while(n!=0):
	res.append(n%10)
	n = n//10
res.sort(reverse=True)

for i in range(len(res)):
        answer+=str(res[i])

print(answer)