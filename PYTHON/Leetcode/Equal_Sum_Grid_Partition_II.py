def canPartitionGrid(grid: list) -> bool:
    def check(x):
        n = len(x)
        m = len(x[0])
        curr = 0 
        seen = {}

        for i in range(n-1):
            for j in range(m):
                v = x[i][j]
                curr += v 
                if v in seen:
                    seen[v][1] = (i, j)
                else:
                    seen[v] = [(i, j), (i, j)]

            diff = total - curr*2
            if diff == 0:
                return True 
            if -diff in seen:
                fr, fc = seen[-diff][0]
                lr, lc = seen[-diff][1]
                if m > 1 and i+1 > 1: return True 
                if m > 1 and i+1 == 1 and (fc == 0 or lc == m-1): return True 
                if m == 1 and (fr == 0 or lr == i): return True 

    n = len(grid)
    m = len(grid[0])
    total = sum(grid[i][j] for j in range(m) for i in range(n))
    if check(grid) or check(grid[::-1]): return True 

    grid = list(zip(*grid))

    if check(grid) or check(grid[::-1]): return True 
    return False
