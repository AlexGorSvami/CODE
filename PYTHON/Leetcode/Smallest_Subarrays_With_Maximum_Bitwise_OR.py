def smallestSubarrays(nums: list) -> list:
    n = len(nums)
    bit_pos = [-1] * 32
    result = [1] * n 

    for i in range(n-1, -1, -1):
        for bit in range(32):
            if (nums[i] >> bit) & 1:
                bit_pos[bit] = i 

        max_pos = i 
        for pos in bit_pos:
            if pos != -1:
                max_pos = max(max_pos, pos)

        result[i] = max_pos - i + 1 

    return result 
