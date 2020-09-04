def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        slice=array[commands[i][0]-1:commands[i][1]]
        slice.sort()
        answer.append(slice[commands[i][2]-1])
    return answer

array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
result = solution(array,commands)
print(result)