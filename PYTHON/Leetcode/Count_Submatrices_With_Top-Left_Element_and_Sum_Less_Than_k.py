def countSubmatrices(grid: list, k: int) -> int:
    import bisect 
    cnt = 0 
    m, n = len(grid), len(grid[0])
    curr = [0] * (n + 1)
    for i in range(m):
        prefix = 0 
        for j in range(n):
            prefix += grid[i][j]
            curr[j+1] += prefix 
        cnt += bisect.bisect_right(curr, k) - 1 
    return cnt 

