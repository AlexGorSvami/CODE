def maximumlength(nums: list) -> int:
    even, odd = 0, 0
    for num in nums:
        if num % 2 == 0:
            even += 1 
        else:
            odd += 1 
    even_dp, odd_dp = 0, 0 
    for num in nums:
        if num % 2 == 0:
            even_dp = max(even_dp, odd_dp + 1)
        else:
            odd_dp = max(odd_dp, even_dp + 1)

    return max(even, odd, even_dp, odd_dp)
