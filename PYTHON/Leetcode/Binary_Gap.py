def binaryGap(n: int) -> int:
    result = 0 
    last = None 
    for i in range(30):
        if n & 1:
            result = result if last is None else max(result, i-last)
            last = i 
        n >>= 1 
    return result 

