def isPowerOfFour(n: int) -> bool:
    if n <= 0:
        return False
    else:
        if n & (n - 1) == 0 and len(bin(n)[3:]) % 2 == 0:
            return True
        else:
            return False 
