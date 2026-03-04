def numSpecial(mat: list) -> int:
    def check(row, col, mat):
        cnt = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if (i == row or j == col):
                    if (mat[i][j] == 1):
                        cnt += 1 
        if (cnt > 1):
            return 0 
        return cnt 

    answer = 0 
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if (mat[i][j] == 1 and check(i, j, mat) == 1):
                answer += 1 

    return answer 
