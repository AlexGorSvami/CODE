def findRotation(mat: list, target: list) -> bool:
    target = tuple(map(tuple, target))
    for _ in range(4):
        if (mat := tuple(zip(*reversed(mat)))) == target:
            return True 
    return False
