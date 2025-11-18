def isOneCharacter(bits: list) -> bool:
    point = 0
    while point < len(bits) - 2:
        point += 1 + bits[point]
    
    return not bool(bits[point])
