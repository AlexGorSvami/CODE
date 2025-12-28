def countNegatives(grid: list) -> int:
    m, n = len(grid), len(grid[0])
    answer = 0 
    i, j = m-1, 0 

    while i >= 0 and j < n:
        if grid[i][j] < 0:
            answer += n - j 
            i -= 1 
        else:
            j += 1 

    return answer 
