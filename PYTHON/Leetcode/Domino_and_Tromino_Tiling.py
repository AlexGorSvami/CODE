def numTilings(n: int) -> int:
    first, second, third = 0, 1, 1

    for _ in range(n-1):
        first, second, third = second, third, (2*third + first) % int(1e9 + 7)
    return third 

print(numTilings(3))
print(numTilings(1))
