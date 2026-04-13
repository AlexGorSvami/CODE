def getMinDistance(nums: list, target: int, start: int) -> int:
    result = float('inf')
    for i in range(len(nums)):
        if nums[i] == target:
            result = min(result, abs(i - start))
    return result 
