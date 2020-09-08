def sumDivisor(num):
    sum=0
    for i in range(1,num+1):
        if num%i==0:
            sum+=i
    print(sum)

num=12
sumDivisor(num)