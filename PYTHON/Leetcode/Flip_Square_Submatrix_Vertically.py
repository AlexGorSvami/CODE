def reverseSubmatrix(grid: list, x: int, y: int, k: int) -> list:
    n = len(grid)
    l = x 
    r = x + k - 1 
    while l < r:
        for i in range(y, y+k):
            grid[l][i], grid[r][i] = grid[r][i], grid[l][i]
        l += 1 
        r -= 1
    return grid
