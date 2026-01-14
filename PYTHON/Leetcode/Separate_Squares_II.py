def separateSquares(squares: list) -> float:
    def union(intervals: list) -> int:
        intervals.sort()
        result, end = 0, -inf
        for a, b in intervals:
            if a > end:
                result += b - a
                end = b 
            elif b > end:
                result += b - end 
                end = b 

        return result 

    events = []
    for x, y, l in squares:
        events.append((y, 1, x, x + l))
        events.append((y + l, -1, x, x + l))

    events.sort()
    xs, prev_y, total_area, areas = [], events[0][0], 0, []
    for y, typ, xl, xr in events:
        h = y - prev_y 
        if h > 0 and xs:
            w = union(xs)
            areas.append((prev_y, h, w))
            total_area += h * w 

        if typ == 1:
            xs.append((xl, xr))
        else:
            xs.remove((xl, xr))

        prev_y = y 

    ac, half = 0, total_area / 2 
    for y, h, w in areas:
        if ac + h * w >= half:
            break 

        ac += h * w 

    return y + (half - ac) / w

