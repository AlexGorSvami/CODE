def maxSideLength(mat: list, threshold: int) -> int:
    if not mat or not mat[0]:
        return 0 
    m, n = len(mat), len(mat[0])
    answer = 0

    #Build 2D prefix sums 
    pref_sums = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            pref_sums[i+1][j+1] = mat[i][j] + pref_sums[i][j+1] + pref_sums[i+1][j] - pref_sums[i][j]

    def sum_square(r: int, c: int, k: int) -> int:
        return pref_sums[r+k][c+k] - pref_sums[r][c+k] - pref_sums[r+k][c] + pref_sums[r][c]
    
    for i in range(m):
        for j in range(n):
            while i + answer < m and j + answer < n and sum_square(i, j, answer+1) <= threshold:
                answer += 1 
    return answer 


