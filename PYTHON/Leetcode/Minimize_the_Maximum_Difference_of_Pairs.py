def minimizeMax(nums: list, p: int) -> int:
    nums.sort()

    def can_pairs(max_diff):
        cnt = 0
        i = 0
        while i < len(nums) -1:
            if abs(nums[i+1] - nums[i]) <= max_diff:
                cnt += 1
                i += 2
            else:
                i += 1 
        return cnt >= p 

    left, right = 0, nums[-1] - nums[0]
    while left < right:
        mid = (left + right) // 2 
        if can_pairs(mid):
            right = mid 
        else:
            left = mid + 1 
    return left 
