def countServers(grid:list) -> int:
    x, y = list(map(sum, grid)), list(map(sum, zip(*grid)))
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and x[i] + y[j] > 2:
                result += 1
    return result 


print(countServers([[1,0], [0,1]]))
print(countServers([[1,0], [1,1]]))
print(countServers([[1,1,0,0],[0,0,1,0], [0,0,1,0],[0,0,0,1]]))
