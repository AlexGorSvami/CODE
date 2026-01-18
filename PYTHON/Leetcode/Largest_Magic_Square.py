def largestMagicSquare(grid: list) -> int:
    n, m, answer = len(grid), len(grid[0]), 1 

    def valid(i: int, j: int, k: int) -> bool:
        s = None 
        for x in range(i, i + k):
            row = sum(grid[x][j:j+k])
            if s is None:
                s = row 
            elif s != row:
                return False 
        for y in range(j, j + k):
            if sum(grid[x][y] for x in range(i, i + k)) != s:
                return False 
        if sum(grid[i + d][j + d] for d in range(k)) != s:
            return False 
        if sum(grid[i + d][j+k-1-d] for d in range(k)) != s:
            return False 
        return True 

    for k in range(2, min(n, m) + 1):
        for i in range(n-k+1):
            for j in range(m-k+1):
                if valid(i, j, k):
                    answer = k 

    return answer 
