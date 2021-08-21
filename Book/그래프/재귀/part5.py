N=3
def func_C(level):
    if level>=N:
        return

    print(level,end=" ")
    func_C(level+1)
    print(level,end=" ")
    func_C(level + 1)
    print(level, end=" ")

if __name__ == '__main__':
    func_C(0)