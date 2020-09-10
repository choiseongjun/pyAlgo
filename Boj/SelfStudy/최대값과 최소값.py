def getMinMaxString(str):
    li=[]

    max = -24700000
    min = 2470000
    for i in str.split():
        i=int(i)
        if min>i:
            min=i
        if max<i:
            max=i

    print(min,max)


str="1 2 3 4"
getMinMaxString(str)