def isValidSudoku(board: list) -> bool:
    vec = [set() for _ in range(27)]
    for i, j in enumerate(board):
        for k, l in enumerate(j):
            if l != '.':
                if l in vec[i] or l in vec[k+9] or l in vec[18 + i//3*3 + k//3]:
                    return False
                vec[i] |= {l}
                vec[k+9] |= {l}
                vec[18 + i//3*3 + k//3] |= {l}
    return True
