def makeTheIntegerZero(num1: int, num2: int) -> int:
    for i in range(1, 61):
        x = num1 - num2 * i 
        if x < i:
            return -1
        if bin(x).count('1') <= i:
            return i 
        return -1
