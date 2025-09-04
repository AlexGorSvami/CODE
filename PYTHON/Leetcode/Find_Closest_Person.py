def findClosest(x: int, y: int, z: int) -> int:
    dist_x, dist_y = abs(x - z), abs(y - z)

    if dist_x == dist_y:
        return 0
    return 1 if dist_x < dist_y else 2
