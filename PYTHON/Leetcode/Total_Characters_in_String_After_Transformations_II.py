def lengthAfterTransformations(s: str, t: int, nums: list) -> int:
    if t == 0:
        return len(s) % (10**9 + 7)

    mod = 10**9 + 7
    n = 26

    def mul(a, b):
        result = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if a[i][j]:
                    for k in range(n):
                        if b[j][k]:
                            result[i][k] = (result[i][k] + (a[i][j] * b [j][k])) % mod 
        return result 

    def math_pow(math, pow):
        if pow == 0:
            return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        if pow == 1:
            return math 

        half = math_pow(math, pow // 2)
        if pow % 2 == 0:
            return mul(half, half)
        return mul(mul(half, half), math)

    trans = [[0] * n for _ in range(n)]
    for i in range(n):
        num = nums[i]
        if num:
            for j in range(num):
                next_char = (i + j + 1) % n 
                trans[i][next_char] = 1 
    char_count = [0] * n 
    for c in s:
        char_count[ord(c) - ord('a')] += 1 

    final = math_pow(trans, t)

    result = 0 
    for i in range(n):
        if char_count[i]:
            for j in range(n):
                if final[i][j]:
                    result = (result + (char_count[i] * final[i][j])) % mod 
    return result 
