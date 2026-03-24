def constructProductMatrix(grid: list) -> list:
    m = len(grid)
    n = len(grid[0])
    prev = 1 
    answer = [[0] * n for _ in range(m)]
    for row in range(m):
        for col in range(n):
            answer[row][col] = prev 
            prev *= grid[row][col] % 12345 
            prev %= 12345 

    prev = 1 
    for row in range(m-1, -1, -1):
        for col in range(n-1, -1, -1):
            answer[row][col] *= prev 
            answer[row][col] %= 12345 
            prev *= grid[row][col] % 12345 
            prev %= 12345 

    return answer 
