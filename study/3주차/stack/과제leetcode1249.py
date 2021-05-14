def minRemoveToMakeValid(s):

    stack = []
    answer = []

    for i,e in enumerate(s):
        answer.append(e)
        if e == '(':
            stack.append((i,e))
        elif e == ')':
            if stack and stack[-1][1] == '(':
                stack.pop()
            else:
                stack.append((i,e))

        for e in stack[::-1]:
            answer.pop(e[0])

        return ''.join(answer)


if __name__ == '__main__':
    s="lee (t (c) o) de)"
    res = minRemoveToMakeValid(s)
    print(res)