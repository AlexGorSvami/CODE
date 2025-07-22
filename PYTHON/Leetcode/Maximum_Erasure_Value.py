def maximumUniqueSubarray(nums: list) -> int:
    answer = 0
    l = s = 0
    memory = {}
    n = len(nums)
    for i in range(n):
        s += nums[i]

        while l < i and nums[i] in memory:
            s -= nums[l]
            del memory[nums[l]]
            l += 1 
        memory[nums[i]] = i 
        answer = max(answer, s)
    
    return answer
