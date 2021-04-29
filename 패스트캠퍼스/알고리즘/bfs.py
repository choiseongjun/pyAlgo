
def bfs(graph,start_node):

    visited=list()#최종적으로 들어갈거
    need_visit=list()#다넣는거

    need_visit.append(start_node)

    while need_visit:
        node=need_visit.pop(0)
        if node not in visited:
            print(graph[node])
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

def dfs(graph,start_node):
    visited,need_visit=list(),list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited


if __name__ == '__main__':
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }
    res = bfs(graph, 'A')
    res1 = dfs(graph,'A')
    print(res)
    print(res1)