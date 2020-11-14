
price=[1, 2, 3, 2, 3]
plen = len(price)
answer=[0]*plen

for i in range(len(price)):
    for j in range(i+1,len(price)):
        if price[i]<=price[j]:
            answer[i]+=1
        else:
            answer[i]+=1
            break
    print(answer)