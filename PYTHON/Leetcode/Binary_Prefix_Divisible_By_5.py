def prefixDivBy5(nums: list) -> list:
    result = []
    num = 0
    for bit in nums:
        num = ((num << 1) | bit) % 5 
        result.append(num == 0)

    return result 
