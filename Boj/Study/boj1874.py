N = int(input())
num_seq_list = []
seq_count = 0
for i in range(N):
    num_seq_list.append(int(input()))

def make_sequence(n, num_seq_list):
    my_stack = []                                                   #스택
    output_result = []                                              #+, - 저장할 리스트
    stack_count = 0                                                 #스택에 추가하는 원소 값을 카운팅
    seq_count = 0                                                   #주어진 수열의 인덱스를 카운팅
    for i in range(n):
        if num_seq_list[seq_count] > stack_count:                   #수열의 다음 원소가 더 큰 경우
            while num_seq_list[seq_count] > stack_count:            #스택에 계속 추가
                stack_count += 1
                my_stack.append(stack_count)
                output_result.append("+")
            my_stack.pop()                                          #해당 원소는 바로 다시 pop
            seq_count += 1
            output_result.append("-")
        else:
            last_index = len(my_stack) - 1
            if num_seq_list[seq_count] == my_stack[last_index]:     #만약 스택 마지막 원소와 같은 값이면
                output_result.append("-")
                my_stack.pop()                                      #그 원소는 pop
                seq_count += 1
            else:                                                   #스택 마지막 원소보다 작은 값은 꺼내기 불가능. 즉시 함수 종료.
                return ['NO']
    return output_result

output_result = make_sequence(N, num_seq_list)                      #output 처리
for letter in output_result:
    print(letter)