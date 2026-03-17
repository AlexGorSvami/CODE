def getBiggestThree(grid: list) -> list:
    res = set()
    row = len(grid)
    col = len(grid[0])
    for i in range(row):
        for j in range(col):
            res.add(grid[i][j])
            if len(res) > 3:
                res.remove(min(res))

            for k in range(1, min(row, col)):
                if i - k >= 0 and i + k < row and j - k >= 0 and j + k < col:
                    total = 0 
                    for x in range(k):
                        y = k - x 
                        total += (grid[i-x][j+y] + grid[i+y][j+x] + grid[i+x][j-y] + grid[i-y][j-x])
                    res.add(total)
                    if len(res) > 3:
                        res.remove(min(res))

    return sorted(res, reverse=True)
