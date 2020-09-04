def arrayPairSum(a):
        a.sort()
        pair=[]
        sum=0
        for i in a:
            pair.append(i)
            if len(pair)==2:
                sum+=min(pair)
                pair=[]
        return sum


if __name__=="__main__":
    a=[1,4,3,2]
    b=arrayPairSum(a)
    print(b)