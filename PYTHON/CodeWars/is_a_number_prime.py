# def is_prime(num):
#     if num < 2:
#         return False
#     if num > 1:
#         for i in range(2, num//2 + 1):
#             if num % i == 0:
#                 return False
#         return True

from math import sqrt
def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i <= sqrt(num):
        if num % i == 0:
            return False
        i += 1
    return True
