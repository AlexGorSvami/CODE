def square_digits(num):
    res = ''
    for i in str(num):
        res += str(int(i)**2)
    res = int(res)
    return res

print(square_digits(9119))
