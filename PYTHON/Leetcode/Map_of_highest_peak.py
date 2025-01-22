from collections import deque 

def highestPeak(isWater: list) -> list:
    m, n = len(isWater), len(isWater[0])
    queue = deque()
    heights = [[-1] * n for _ in range(m)]
        
    for row in range(m):
        for col in range(n):
            if isWater[row][col] == 1:
                queue.append((row, col, 0))  
        
    while queue:
        x, y, height = queue.popleft()
        if heights[x][y] != -1:  
            continue
        heights[x][y] = height  
            
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] == -1:
                queue.append((nx, ny, height + 1))
        
    return heights


print(highestPeak([[0,1],[0,0]]))
print(highestPeak([[1,1,0], [0,1,1], [1,2,2]]))
