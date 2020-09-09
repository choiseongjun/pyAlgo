def fibonachi(n):
    list=[]
    for i in range(0,n):
        if i<2:
            list.append(1)
        else:
            list.append(list[i-1]+list[i-2])
        return list[n-1]

n=4
result = fibonachi(n)
print(result)


def fibo(n):
    if n<3:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)