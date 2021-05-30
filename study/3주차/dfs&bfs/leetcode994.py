from collections import deque


def orangesRotting(grid):
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    rotten = 2
    fresh = 1
    empty = 0

    if len(grid)==0:
        return 0

    queue = deque([])
    freshOranges = 0
    # collect all the rotten oranges and fresh oranges at the beginning
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == rotten:
                queue.append([row, col])
            if grid[row][col] == fresh:
                freshOranges += 1

    curQueueSize = len(queue)
    minutes = 0
    print(curQueueSize)
    # while len(queue) > 0:
    #     if curQueueSize == 0:
    #         minutes += 1
    #         curQueueSize = len(queue)



if __name__ == '__main__':
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    orangesRotting(grid)