def swimInWater(grid: list) -> int:
    n = len(grid)
    delta = (-1, 0, 1, 0, -1)
    data = {(i, j) : (i, j) for i in range(n) for j in range(n)}

    def find(x):
        if x != data[x]:
            data[x] = find(data[x])
        return data[x]

    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx != ry:
            data[rx] = ry

    def expand(i, j):
        for k in range(4):
            ni, nj = i + delta[k], j + delta[k + 1]
            if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] <= grid[i][j]:
                union((i, j), (ni, nj))

    cells = sorted((grid[i][j], i, j) for i in range(n) for j in range(n))
    for level, i, j in cells:
        expand(i, j)
        if find((0, 0)) == find((n - 1, n - 1)):
            return level
    assert(False)
