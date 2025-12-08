def countTriples(n: int) -> int:
    from math import sqrt
    square = 0 
    for a in range(1, n):
        for b in range(a, n):
            c = sqrt(a**2 + b**2)
            if c > n:
                break 
            elif c.is_integer():
                if a == b:
                    square += 1 
                else:
                    square += 2 

    return square 
