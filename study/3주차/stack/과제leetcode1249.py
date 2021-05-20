def minRemoveToMakeValid(s):
    stack = []
    ans = []

    # 1. find all brackets
    for idx, value in enumerate(s):
        ans.append(value)
        if value == '(':#(이면 인덱스와 밸류를 넣는
            stack.append((idx, value))
        elif value == ')':
            if stack and stack[0][1] == '(':#스택에 처음담긴걸 뺴버린다.
                stack.pop()
            else:
                stack.append((idx, value))
    #유효하지 않은 괄호를 뺴버린다
    for e in stack[::-1]:
        ans.pop(e[0])

    return ''.join(ans)


if __name__ == '__main__':
    s="(a(b(c)d)"
    res = minRemoveToMakeValid(s)
    print(res)