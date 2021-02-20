
def fibo(a):

    if a<2:
        return a
    else:
        return fibo(a-1)+fibo(a-2)


a= 10
n=10
sum=0
sum+=fibo(a)
print(sum)

