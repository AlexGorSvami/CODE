def separateSquares(squares: list) -> float:
    total = sum(l * l for _, _, l in squares)
    target = total/2 
    events = []

    for _, y, l in squares:
        events.append((y, l))
        events.append((y + l, -l))

    events.sort()
    curr_area = 0.0
    curr_width = 0.0 
    last_y = squares[0][0]

    for y, delta in events:
        if y > last_y:
            segment = curr_width * (y - last_y)
            if curr_area + segment >= target:
                need = target - curr_area 
                return last_y + (need /curr_width) 
            
            curr_area += segment 

        last_y = y 
        curr_width += delta 

    return float(last_y)

