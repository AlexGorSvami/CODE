def smallestRepunitDivByK(k: int) -> int:
    if k == 1:
        return 1 

    remainder = [False for _ in range(k)]
    curr = res = 1 

    while True:
        curr = (curr * 10 + 1) % k 
        res += 1 
        if curr == 0:
            return res 
        elif remainder[curr]:
            break 
        remainder[curr] = True 

    return -1 
