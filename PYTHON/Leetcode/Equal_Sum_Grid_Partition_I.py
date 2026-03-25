def canPartitionGrid(grid: list) -> bool:
    rows = []
    rows_total = 0
    for row in grid:
        rows_total += sum(row)
        rows.append(rows_total)
    if rows_total / 2 in rows:
        return True 

    cols = []
    cols_total = 0 
    for j in range(len(grid[0])):
        col_total = 0 
        for i in range(len(grid)):
            cols_total += grid[i][j]
        cols_total += col_total 
        cols.append(cols_total)
    return cols_total / 2 in cols 
