def findKthBit(n: int, k: int) -> str:
    curr = n 
    invertor = 0 
    k -= 1
    while curr > 1:
        middle = 2 ** (curr - 1) - 1 
        if k == middle:
            return '0' if invertor % 2 else '1'
        if k > middle:
            invertor += 1 
            k = 2 * middle - k 
        curr -= 1 

    return '1' if invertor % 2 else '0'
