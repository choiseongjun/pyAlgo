

def dfs(node,network,visited):
    visited.add(node)
    print(visited)
    for x in network[node]:
        print(x)
        if x not in visited:
            dfs(x,network,visited)



def makeConnected(n, connections):

    if len(connections) < n - 1:
        return -1

    network = [[] for _ in range(n)]

    for a, b in connections:
        network[a].append(b)
        network[b].append(a)

    group = [0] * n
    curgroup = 0

    for node in range(n):
        if not group[node]:
            curgroup+=1
            visited=set()
            dfs(node,network,visited)
            for i in visited:
                group[i] = curgroup
                #print(group,curgroup)
    return curgroup-1


# def dfs(node,network,visited):
#     visited.


if __name__ == '__main__':
    n = 4
    connections = [[0,1],[0,2],[1,2]]
    res = makeConnected(n,connections)
    print(res)