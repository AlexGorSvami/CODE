def numSteps(s: str) -> int:
    result = 0 
    num = int(s, 2)
    while num != 1:
        if num & 1:
            num += 1 
        else:
            num >>= 2 
        result += 1
    return result
