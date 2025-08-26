def areaOfMaxDiagonal(dimensions: list) -> int:
    return max((x*x + y*y, x*y) for x,y in dimensions)[1]
