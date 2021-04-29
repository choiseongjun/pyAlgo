a = "ababababa"
b = "aba"

index=0
result=0

while len(a)-index>=len(b):
    if a[index:index+len(b)] == b:
        index+=len(b)
        result+=1
    else:
        index+=1
print(result)