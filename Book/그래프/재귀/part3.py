N=5
def func_A(level):
    if level >= N:
        return
    #print(level)
    func_A(level + 1)
    print(level,end=" ")

    return
func_A(0)