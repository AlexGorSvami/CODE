def reverse(x:int) -> int:
    negative = x < 0
    x = abs(x)

    reversed_num = 0
    while x > 0:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    
    if reversed_num > 2**31 -1 or reversed_num < -2**31:
        return 0

    if negative:
        return -reversed_num

    return reversed_num

print(reverse(321))
print(reverse(-130))
print(reverse(543))
