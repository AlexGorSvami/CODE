def count_bits(n):
    res = 0
    for i in bin(n)[2:]:
        if i != '0':
            res += 1
    return res

def count_bits1(n):
    return bin(n).count('1')
