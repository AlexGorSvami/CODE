def xorAfterQueries(nums: list, queries: list) -> int:
    MOD = 10**9 + 7 
    for left, right, i, j in queries:
        for k in range(left, right+1, i):
            nums[k] = (nums[k] * j) % MOD 

    result = 0 
    for i in nums:
        result ^= i 

    return result
