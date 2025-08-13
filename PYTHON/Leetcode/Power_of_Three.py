def isPowerOfThree(n: int) -> bool:
    if n > 0 and 1162261467 % n == 0:
        return True
    return False
