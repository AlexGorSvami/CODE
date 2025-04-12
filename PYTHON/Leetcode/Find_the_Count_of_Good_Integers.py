def countGoodIntegers(n: int, k: int) -> int:
    from collections import Counter 
    from math import factorial 

    half_len = (n + 1) // 2 
    total = 0
    seen_palindromes = set()

    for half_len in range(10**(half_len - 1), 10**half_len):
        full_palindrom = str(half_len) + str(half_len)[::-1][n % 2:]

        sort_key = ''.join(sorted(full_palindrom))

        if int(full_palindrom) % k == 0 and sort_key not in seen_palindromes:
            seen_palindromes.add(sort_key) 

            digit_count = Counter(full_palindrom)
            permutation_count = (n - digit_count['0']) * factorial(n - 1)
            for cnt in digit_count.values():
                permutation_count //= factorial(cnt)
            total += permutation_count 

    return total
print(countGoodIntegers(3,5))
print(countGoodIntegers(1,4))
