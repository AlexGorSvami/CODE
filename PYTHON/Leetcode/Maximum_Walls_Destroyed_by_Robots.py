def maxWalls(robots: list, distance: list, walls: list) -> int:
    n = len(robots)
    array = sorted(zip(robots, distance), key=lambda x: x[0])
    walls.sort()

    @cache 
    def dfs(i: int, j: int) -> int:
        if i < 0: 
            return 0 
        left = array[i][0] - array[i][1]
        l = bisect_left(walls, left)
        r = bisect_left(walls, array[i][0] + 1)
        answer = dfs(i - 1, 0) + r - l 
        right = array[i][0] + array[i][1]
        if i + 1 < n:
            if j == 0:
                right = min(right, array[i+1][0] - array[i+1][1]-1)
            else:
                right = min(right, array[i+1][0]-1)
        l = bisect_left(walls, array[i][0])
        r = bisect_left(walls, right+1)
        answer = max(answer, dfs(i-1, 1) + r - l)
        return answer 

    answer = dfs(n-1, 1)
    dfs.cache_clear()
    return answer 
