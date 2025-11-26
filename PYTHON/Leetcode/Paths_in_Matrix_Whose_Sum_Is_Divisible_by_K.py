def numberOfPaths(grid: list, k: int) -> int:
    memo = [[[-1]*k for _ in range(len(grid[0]))] for _ in range(len(grid))]
    def dfs(i , j , total):
        if i == len(grid)-1 and j == len(grid[0])-1:
            return 1 if (grid[i][j] + total) % k == 0 else 0
        if i == len(grid) or j == len(grid[0]):
            return 0
        if memo[i][j][total] != -1:
            return memo[i][j][total]
        else:
            left = dfs(i+1 ,j , (grid[i][j] + total)%k)
            right = dfs(i , j+1 , (grid[i][j] + total)%k)
            memo[i][j][total]=  left+right
            return memo[i][j][total]





    return dfs(0,0,0) % (10 ** 9 + 7)
