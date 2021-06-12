from typing import List


def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    visited = set()
    def dfs(room):
        if room in visited:
            return
        visited.add(room)
        for r in rooms[room]:
            dfs(r)
    dfs(0)
    return len(visited) == len(rooms)

if __name__ == '__main__':
    a = [[1,3],[3,0,1],[2],[0]]
    res = canVisitAllRooms(a)
    print(res)



