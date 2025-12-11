def countCoveredBuildings(n: int, buildings: list) -> int:
    from collections import defaultdict 

    h1, h2 = defaultdict(lambda : [float('inf'), float('-inf')]), defaultdict(lambda: [float('inf'), float('-inf')])

    for x, y in buildings:
        h1[x] = [min(h1[x][0], y), max(h1[x][1], y)]
        h2[y] = [min(h2[y][0], x), max(h2[y][1], x)]

    return sum(h1[x][0] < y < h1[x][1] and h2[y][0] < x < h2[y][1] for x, y in buildings)
