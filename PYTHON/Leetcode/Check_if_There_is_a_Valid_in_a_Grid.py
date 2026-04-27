def hasValidPath(grid):
    m, n = len(grid), len(grid[0])
    
    # Куда ведёт улица (выходы)
    dirs = {
        1: [(0,1), (0,-1)],   # право, лево
        2: [(1,0), (-1,0)],   # низ, верх
        3: [(1,0), (0,-1)],   # низ, лево
        4: [(1,0), (0,1)],    # низ, право
        5: [(-1,0), (0,-1)],  # верх, лево
        6: [(-1,0), (0,1)]    # верх, право
    }
    
    # Какие улицы можно пройти, заходя с данного направления
    opposite = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
    compatible = {
        'up': [2,5,6], 'down': [2,3,4],
        'left': [1,3,5], 'right': [1,4,6]
    }
    
    q = [(0,0)]
    seen = {(0,0)}
    
    while q:
        x,y = q.pop()
        if (x,y) == (m-1,n-1): return True
        
        for dx,dy in dirs[grid[x][y]]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in seen:
                # Определяем сторону входа в соседнюю клетку
                if dx == 1: side = 'up'
                elif dx == -1: side = 'down'
                elif dy == 1: side = 'left'
                else: side = 'right'
                
                if grid[nx][ny] in compatible[side]:
                    seen.add((nx,ny))
                    q.append((nx,ny))
    return False
