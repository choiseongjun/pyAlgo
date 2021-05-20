

if __name__ == '__main__':
    stack=[]
    s="123456789"

    for i,e in enumerate(s):
        stack.append((i,e))

    print(stack[-1][1])
