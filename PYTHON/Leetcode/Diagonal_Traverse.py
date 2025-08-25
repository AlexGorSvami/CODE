def findDiagonalOrder(mat: list) -> list:
    d = {}
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i + j not in d:
                d[i+j] = [mat[i][j]]
            else:
                d[i+j].append(mat[i][j])

    answer = []
    for entry in d.items():
        if entry[0] % 2 == 0:
            [answer.append(x) for x in entry[1][::-1]]
        else:
            [answer.append(x) for x in entry[1]]
    return answer 
