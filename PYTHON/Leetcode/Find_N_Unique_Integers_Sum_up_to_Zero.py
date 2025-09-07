def sumZero(n: int) -> list:
    if n == 1:
        return [0]
    result = [] if n % 2 == 0 else [0]
    for i in range(1, (n // 2) + 1):
        result += [i, -i]
    return result 
