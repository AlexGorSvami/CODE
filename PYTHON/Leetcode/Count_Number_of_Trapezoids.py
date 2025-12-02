def countTrapezoids(points: list) -> int:
    if len(points) < 4:
        return 0 

    answer = 0 
    dic_points = defaultdict(int)
    for x, y in points:
        dic_points[y] += 1 

    total, sum_squares = 0, 0 

    for cnt in dic_points.values():
        if cnt >= 2:
            c = math.comb(cnt, 2)
            total += c 
            sum_squares += c*c 

    answer = (total * total - sum_squares) // 2 
    return answer % (10 ** 9 + 7)
