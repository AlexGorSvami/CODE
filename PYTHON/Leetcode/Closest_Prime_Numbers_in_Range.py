def closestPrimes(left: int, right: int) -> list:
    from math import floor, sqrt
    def is_prime(num):
        if num == 1:
            return False 
        for div in range(2, floor(sqrt(num))+1):
            if num % div == 0:
                return False 
        return True

    primes = []
    for pers in range(left, right+1):
        if is_prime(pers):
            if primes and pers <= primes[-1]+2:
                return [primes[-1], pers]
            primes.append(pers)
    
    gaps = ([primes[i-1], primes[i]] for i in range(1, len(primes)))
    return min(gaps, key=lambda x: (x[1] - x[0], x[0]), default=[-1, -1])


print(closestPrimes(10, 19))
print(closestPrimes(4, 6))
