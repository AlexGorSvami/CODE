def idealArrays(n: int, maxValue: int) -> int:
    from functools import cache 
    from math import comb 

    @cache 
    def dp(curr_end: int, size:int) -> int:
        result = comb(n-1, size-1)

        next_end = curr_end << 1 

        if size == n or next_end > maxValue:
            return result 

        while next_end <= maxValue:
            result += dp(next_end, size+1)
            next_end += curr_end 

        return result 

    return sum(
            dp(i, 1)
            for i in range(1, maxValue+1)
            ) % (10**9 + 7)


print(idealArrays(2, 5))
print(idealArrays(5, 3))
