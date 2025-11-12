def minOperations(nums: list) -> int:
    from math import gcd
    n = len(nums)
    ones_cnt = nums.count(1)
    if ones_cnt > 0:
        return n - ones_cnt 
    
    min_len = n + 1 
    for i in range(n):
        current_gcd = 0
        for j in range(i, n):
            current_gcd = gcd(current_gcd, nums[j])

            if current_gcd == 1:
                min_len = min(min_len, j - i + 1)
                break 

    if min_len > n:
        return -1 

    return n + min_len - 2
