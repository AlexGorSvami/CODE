def robotSim(commands: list, obstacles: list) -> int:
    directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
    obs = set(map(tuple, obstacles))
    d = 0 
    pos = [0, 0]
    result = 0 

    for c in commands:
        if c == -2:
            d = (d + 3) % 4 
        elif c == -1:
            d = (d + 1) % 4 
        else:
            for _ in range(c):
                tmpx = pos[0] + directions[d][0]
                tmpy = pos[1] + directions[d][1]
                if (tmpx, tmpy) in obs:
                    break 

                pos = [tmpx, tmpy]

            result = max(result, pos[0] ** 2 + pos[1] ** 2)

    return result 

