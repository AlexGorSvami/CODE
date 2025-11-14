def rangeAddQueries(n: int, queries: list) -> list:
    different = [[0] * (n + 2) for _ in range(n + 2)]
    for r1, c1, r2, c2 in queries:
        different[r1 + 1][c1 + 1] += 1 
        different[r2 + 2][c2 + 2] += 1
        different[r2 + 2][c1 + 1] -= 1 
        different[r1 + 1][c2 + 2] -= 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            different[i][j] += different[i - 1][j] + different[i][j - 1] - different[i - 1][j - 1]

    different = different[1:-1]
    result = [i[1:-1] for i in different]
        
    return result

