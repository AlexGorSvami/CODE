def getHappyString(n: int, k: int) -> str:
    base = 2**(n-1)
    if k > 3*base:
        return ''
    result = [chr(ord('a')+(k-1)//base)]
    while base > 1:
        k -= (k-1)//base*base 
        base //= 2
        result.append(('a' if result[-1] != 'a' else 'b') if (k-1)//base == 0 else ('c' if result[-1] != 'c' else 'b'))

    return ''.join(result)


print(getHappyString(1, 3))
print(getHappyString(1, 4))
print(getHappyString(3, 9))
