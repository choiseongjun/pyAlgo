def removeDuplicates(s):
    stack = []
    for i in s:
        if stack and i==stack[-1]: #스택이 비지 않고 스택양끝을 비교했을떄 같은게 있으면
            stack.pop() #빼버린다
        else:#스택이 비어있으면
            stack.append(i)


    return "".join(stack)



if __name__ == '__main__':
    s = "abbaca"
    res = removeDuplicates(s)
    print(res)