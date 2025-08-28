def sortMatrix(grid: list) -> list:
    n, m = len(grid), len(grid[0])
    diagonals = {}
    for i in range(n):
        for j in range(m):
            key = i - j 
            if key not in diagonals:
                diagonals[key] = []
            if key < 0:
                heapq.heappush(diagonals[key], grid[i][j])
            else:
                heapq.heappush(diagonals[key], -grid[i][j])
    for i in range(n):
        for j in range(m):
            key = i - j 
            if key < 0:
                grid[i][j] = heapq.heappop(diagonals[key])
            else:
                grid[i][j] = -heapq.heappop(diagonals[key])
    return grid 

