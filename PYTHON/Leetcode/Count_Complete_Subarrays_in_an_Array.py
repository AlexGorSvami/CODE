def countCompleteSubarrays(nums: list) -> int:
    result = 0
    n = len(nums)
    n_distinct = len(set(nums))
    mapping = {}
    left, right = 0, 0 
    while left <= right and left < n:
        while len(mapping) < n_distinct and right < n:
            num_add = nums[right]
            mapping[nums[right]] = mapping.get(nums[right], 0) + 1 
            right += 1
        if len(mapping) == n_distinct:
            result += n - right + 1 

        mapping[nums[left]] -= 1

        if mapping[nums[left]] == 0:
            del mapping[nums[left]]
        left += 1 

    return result 



print(countCompleteSubarrays([1,3,1,2,2]))
print(countCompleteSubarrays([5,5,5,5]))
