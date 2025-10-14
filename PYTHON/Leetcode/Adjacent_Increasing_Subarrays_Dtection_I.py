def hasIncreasingSubarrays(nums: list, k: int) -> bool:
    n = len(nums)
    for i in range(k, n-k+1):
        first = nums[i - k:i]
        second = nums[i:i + k]

        if all(first[i] < first[i+1] for i in range(k-1)) and \
           all(second[i] < second[i+1] for i in range(k-1)):
            return True  
    return False
