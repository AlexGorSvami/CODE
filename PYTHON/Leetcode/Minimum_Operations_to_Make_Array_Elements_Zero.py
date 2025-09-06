def minOperations(queries: list) -> int:
    result = 0
    for l, r in queries:
        total = 0
        base = i = 1 
        while base <= r:
            nl = max(l, base)
            nr = min(r, 4*base-1)
            if nl <= nr:
                total += i * (nr-nl+1)
            i += 1 
            base *= 4 
        result += (total+1) // 2 
    return result 
