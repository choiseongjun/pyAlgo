def Qsort(lt,rt):
    if lt<rt:
        pos=lt
        pivot=arr[rt]
        for i in range(lt,rt):
            print(arr)
            if arr[i]<=pivot:
                arr[i],arr[pos]=arr[pos],arr[i]
                pos+=1
        arr[rt],arr[pos]=arr[pos],arr[rt]
        Qsort(lt,pos-1)
        Qsort(pos+1,rt)



45,21,23,36,15,67,11,60,20,33
if __name__ =="__main__":
    arr=[45,21,23,36,15,67,11,60,20,33]
    print("Before sort:",end=' ')
    print(arr)
    Qsort(0,9)
    print("After sort:",end=' ')
    print(arr)

# 퀵소트는 일단 피봇을 맨끝에 잡고 pos와 i를 선언해서 i가 피봇보다 작으면 스와핑한다 그리고 피봇까지 다오면 pos와 피봇값을 스와핑한다 반복하면 정렬되어있다