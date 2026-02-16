def reverseBit(n: int) -> int:
    return int('{0:032b}'.format(n)[::-1], 2)
