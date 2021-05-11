


def dailyTemperatures(T):
    stack =[]
    answer= [0]*len(T)
    for i,cur in enumerate(T):
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            print(last)
            answer[last] = i-last

        #print(i)
        stack.append(i)
    return answer



if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    dailyTemperatures((T))


