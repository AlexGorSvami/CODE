def isTronic(nums: list) -> bool:
    n, ptr = len(nums), 0 

    while ptr < n-1 and nums[ptr] < nums[ptr+1]:
        ptr += 1 
    if ptr == 0 or ptr == n-2:
        return False 

    p = ptr 
    while ptr < n-1 and nums[ptr] > nums[ptr+1]:
        ptr += 1 
    if ptr == p or ptr == n-1:
        return False 

    for left, right in pairwise(nums[ptr:]):
        if left >= right:
            return False 

    return True
