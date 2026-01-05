def maxMatrix(matrix: list) -> int:
    result = 0
    negative_cnt = 0
    min_matrix = float('inf')
    for row in matrix:
        for num in row:
            result += abs(num)
            min_matrix = min(min_matrix, abs(num))
            if num < 0:
                negative_cnt += 1 

    if negative_cnt & 1:
        result -= 2 * min_matrix 

    return result 
