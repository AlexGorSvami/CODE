bitwiseComplement(n: int) -> int:
    if n == 0:
        return 1 
    lead = 1 << int(math.log(n, 2))
    mask = (lead << 1) - 1 
    return (~n) & mask 
