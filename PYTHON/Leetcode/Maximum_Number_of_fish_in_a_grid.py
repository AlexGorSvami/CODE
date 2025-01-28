def findMaxFish(grid: list) -> int:
    rows, cols = len(grid), len(grid[0])
    visits = set()

    def dfs(r, c):
        if r >= rows or r < 0 or c >= cols or c < 0 or (r, c) in visits or grid[r][c] == 0:
            return 0
        visits.add((r,c))
        fish_cnt = grid[r][c]
        for dr, dc in [(0,1), (1,0), (0, -1), (-1, 0)]:
            fish_cnt += dfs(r + dr, c + dc)
        return fish_cnt 

    max_fish = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0 and (r, c) not in visits:
                max_fish = max(max_fish, dfs(r, c))
    return max_fish 



print(findMaxFish([[0,2,1,0], [4,0,0,3], [1,0,0,4], [0,3,2,0]]))
print(findMaxFish([[1,0,0,0], [0,0,0,0],[0,0,0,0,], [0,0,0,1]]))
