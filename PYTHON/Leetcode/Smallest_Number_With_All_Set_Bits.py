def smallestNumber(n: int) -> int:
    return (1 << n.bit_length()) - 1
