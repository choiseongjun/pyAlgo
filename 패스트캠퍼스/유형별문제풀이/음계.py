
a = list(map(int,input().split()))

asc = True
dsc = True

for i in range(1,8):
    if a[i]>a[i-1]:
        dsc = False
    elif a[i]<a[i-1]:
        asc = False

if asc:
    print('ascending')
elif dsc:
    print('descending')
else:
    print('mixed')