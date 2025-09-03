def numberOfPairs(points: list) -> int:
    points.sort(key=lambda x: (x[0], -x[1]))
    out = 0
    for i in range(len(points)):
        upper_y = float('-inf')
        for j in range(i+1, len(points)):
            if points[i][1] < points[j][1] or points[j][1] <= upper_y:
                continue
            upper_y = max(upper_y, points[j][1])
            out += 1 
    return out 
