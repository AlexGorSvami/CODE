def firstCompleteIndex(arr: list, mat:list) -> int:
    count_rows = len(mat)
    count_cols = len(mat[0])

    rows = [0] * count_rows 
    cols = [0] * count_cols 

    positions = {}
    
    for row in range(count_rows):
        for col in range(count_cols):
            positions[mat[row][col]] = (row, col)

    for indx, num in enumerate(arr):
        row, col = positions[num]
        rows[row] += 1
        cols[col] += 1

        if rows[row] == count_cols or cols[col] == count_rows:
            return indx

    return -1

print(firstCompleteIndex([1,3,4,2], [[1,4], [2,3]]))
print(firstCompleteIndex([2,8,7,4,1,3,5,6,9], [[3,2,5], [1,4,6],[8,7,9]]))

