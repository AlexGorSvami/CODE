def gridGame(grid: list) -> int:
    result = float("inf")
    left, right = 0, sum(grid[0])

    for r, l in zip(grid[0], grid[1]):
        right -= r 
        result = min(result, max(left, right))
        left += l 
    return result 





print(gridGame([[2,5,4], [1,5,1]]))
print(gridGame([[3,3,1],[8,5,2]]))
