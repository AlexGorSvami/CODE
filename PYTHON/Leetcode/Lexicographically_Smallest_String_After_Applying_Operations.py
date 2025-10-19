def findLexSmallestString(s: str, a: int, b: int) -> str:
    n = len(s)
    result = s 
    s = s + s 
    gcd = math.gcd(b, n)

    def add(st, start):
        original = int(st[start])
        min_value, times = 10, 0 
        for i in range(10):
            added = (original + i * a) % 10 
            if added < min_value:
                min_value = added 
                times = i 
        list_st = list(st)
        for i in range(start, n, 2):
            list_st[i] = str((int(list_st[i]) + times * a) % 10)
        return ''.join(list_st)

    for i in range(0, n, gcd):
        t = s[i: i + n]
        t = add(t, 1)
        if b % 2:
            t = add(t, 0)
        if t < result:
            result = t 
        
    return result 
