def minTimeVisitAllPoints(points: list) -> int:
    return sum(max(abs(i[0] - j[0]), abs(i[1] - j[1])) for i, j in zip(points[:-1], points[1:]))
