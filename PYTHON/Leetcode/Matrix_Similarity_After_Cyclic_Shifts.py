def areSimilar(mat: list, k: int) -> bool:
    n = len(mat)
    m = len(mat[0])

    for i in range(0, n, 2):
        for j in range(m):
            index = (j + k) % m 
            if mat[i][j] != mat[i][index]:
                return False 
    for i in range(1, n, 2):
        for j in range(m):
            index = (j - k + m) % m 
            if mat[i][j] != mat[i][index]:
                return False 
    return True 
