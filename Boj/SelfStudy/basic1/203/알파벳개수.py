cnt = [0]*26
for c in input():
    cnt[ord(c)-97] +=1
for n in cnt:
    print(n,end=' ')