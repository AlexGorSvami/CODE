def minimumOneBitOperations(n: int) -> int:
    res, k, mask = 0, 0, 1 
    while mask <= n:
        if n & mask:
            res = 2 ** (k + 1) - 1 - res 
        mask <<= 1 
        k += 1 
        
    return res 
