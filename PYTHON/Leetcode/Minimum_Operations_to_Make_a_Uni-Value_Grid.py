def minOperations(grid: list, x: int) -> int:
        values = sorted([val for row in grid for val in row])
        n = len(values)

        if n == 1:
            return 0

        if not all([val % x == values[0] % x for val in values]):
            return -1

        return sum([abs(values[n // 2] - val) // x for val in values])
