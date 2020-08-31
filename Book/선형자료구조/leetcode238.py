def mul(li):
    out=[]
    p=1
    #왼쪽부터 곱해서 result 추가 [1,1,2,6]
    for i in range(0,len(li)):
        out.append(p)
        p=p*li[i]
    p=1
    #오른쪾부터 시작 [24,12,4,1]
    for i in range(len(li)-1,0-1,-1):
        out[i]=out[i]*p
        p=p*li[i]
    return out


li=[1,2,3,4]
print(mul(li))