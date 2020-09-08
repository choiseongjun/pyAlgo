def toWeirdCase(s):
    result=""
    for i, v in enumerate(s):
        if i % 2:  # 홀수
            result += v.lower()
        else:  # 짝수
            result += v.upper()
    return result


s="try hello world"
toWeirdCase(s)