def differenceOfSums(n: int, m: int) -> int:
    all = n * (n+1) // 2 
    divisible = m * (n // m) * (n // m+1) // 2 
    return all-2 * divisible 
