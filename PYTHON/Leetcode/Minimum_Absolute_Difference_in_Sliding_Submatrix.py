def minAbsDiff(grid: list, k: int) -> list:
    rows, cols = len(grid), len(grid[0])
    result = [[0] * (cols - k + 1) for _ in range(rows - k + 1)]

    for i in range(rows - k + 1):
        for j in range(cols - k + 1):
            values = set()
            for x in range(i, i + k):
                for y in range(j, j + k):
                    values.add(grid[x][y])

            arr = sorted(values)
            if len(arr) <= 1:
                result[i][j] = 0 
                continue 

            min_diff = float('inf')
            for l in range(len(arr) - 1):
                min_diff = min(min_diff, arr[l+1] - arr[l])

            result[i][j] = min_diff 

    return result 
