def minCost(grid: list) -> int:
    from collections import deque

    len_grid, len_first = len(grid), len(grid[0])
    deltas = [(0,1), (0,-1), (1,0), (-1, 0)]
    queue = deque([(0, 0, 0)])
    costs = {}

    while queue:
        row, col, cost = queue.popleft()
        while 0 <= row < len_grid and 0 <= col < len_first and (row, col) not in costs:
            costs[row, col] = cost
            queue += [(row+dr, col+dc, cost+1) for dr, dc in deltas]
            dr, dc = deltas[grid[row][col] - 1]
            row, col = row+dr, col+dc

    return costs[len_grid-1, len_first-1]


print(minCost([[1,1,1,1], [2,2,2,2], [1,1,1,1], [2,2,2,2]]))
print(minCost([[1,1,3], [3,2,2], [1,1,4]]))

