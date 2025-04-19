def countFairPairs(nums: list, lower: int, upper: int) -> int:
    def count(x):
        cnt = 0
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] + nums[right] <= x:
                cnt += right - left 
                left += 1 
            else:
                right -= 1 
        return cnt 
    nums.sort()
    return count(upper) - count(lower-1)


print(countFairPairs([0,1,7,4,4,5], 3, 6))
