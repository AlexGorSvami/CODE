def countSquares(matrix: list) -> int:
    m, n = len(matrix), len(matrix[0])
    answer = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1 and i > 0 and j > 0:
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1 
            answer += matrix[i][j]
    return answer 

