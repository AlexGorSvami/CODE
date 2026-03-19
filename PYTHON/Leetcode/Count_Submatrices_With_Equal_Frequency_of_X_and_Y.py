def numberOfSubmatrices(grid: list) -> int:
    n = len(grid[0])
    answer = 0 
    x = [0] * n 
    y = [0] * n 

    for i in grid:
        rx, ry = 0, 0 
        for j in range(n):
            rx += i[j] == 'X'
            ry += i[j] == 'Y'
            x[j] += rx 
            y[j] += ry 
            answer += (x[j] > 0) & (x[j] == y[j])

    return answer
