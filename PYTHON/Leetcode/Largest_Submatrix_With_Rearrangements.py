def largestSubmatrix(matrix: list) -> int:
    result = 0 
    for i in range(1, len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]:
                matrix[i][j] += matrix[i-1][j]
    for row in matrix:
        row.sort(reverse=True)
        for j in range(len(row)):
            result = max(result, (j+1) * row[j])
    return result 
