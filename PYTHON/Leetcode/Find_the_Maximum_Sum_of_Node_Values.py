def maximumValueSum(nums: list, k: int, edges: list) -> int:
    changed = []
    for i in range(len(nums)):
        changed.append((nums[i] ^ k) - nums[i])

    changed.sort(reverse = True)
    value = sum(nums)

    for i in range(0, len(changed)-1, 2):
        delta = changed[i] + changed[i+1]
        if delta > 0:
            value += delta 
        else:
            return value 

    return value 
