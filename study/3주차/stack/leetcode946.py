def validateStackSequences(pushed, popped):
    stack=[]
    pos=0
    check=False
    for x in pushed:
        stack.append(x)
        while stack and stack[-1] == popped[pos]:
            pos+=1
            stack.pop()
    if len(stack)==0:
        check = True

    return check



if __name__ == '__main__':
    pushed = [1, 2, 3, 4, 5]
    popped = [4,5,3,2,1]
    res = validateStackSequences(pushed,popped)
    print(res)