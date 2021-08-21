N=3
subset = [0]*N

def DFS_a(level):

    if level>=N:
        print(subset)
        return

    subset[level] = 0
    DFS_a(level+1)
    subset[level] = 1
    DFS_a(level + 1)

if __name__ == '__main__':
    DFS_a(0)