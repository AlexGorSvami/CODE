def countPrimeSetBits(left: int, right: int) -> int:
    return sum(665772 >> bin(i).count('1') & 1 for i in range(left, right+1))
