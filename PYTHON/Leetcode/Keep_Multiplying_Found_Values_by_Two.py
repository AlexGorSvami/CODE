def findFinalValue(nums: list, original: int) -> int:
    nums = set(nums)
    while original in nums:
        original <<= 1 
    return original 
