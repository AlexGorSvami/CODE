def getNoZeroIntegers(n: int) -> list:
    if n == 2:
        return [1, 1]
    if n == 3:
        return [1, 2]
    n1 = n // 2 
    for i in range(1, n1):
        n2 = n - i 
        if '0' not in str(i) and '0' not in str(n2):
            return [i, n2]

