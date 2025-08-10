def reorderedPowerOf2(n: int) -> bool:
    n = str(n)
    leng = len(list(n))
    pow_arr = []
    base = 1 

    while True:
        base_str = str(base)
        count_length = len(base_str)
        if count_length == leng:
            pow_arr.append(''.join(sorted(base_str)))
        elif count_length > leng:
            break 
        base <<= 1 

    n = ''.join(sorted(n))
    return n in pow_arr 

