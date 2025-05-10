def minSum(nums1: list, nums2: int) -> int:
    x1, x2 = nums1.count(0), nums1.count(0)
    s1, s2 = sum(nums1), sum(nums2)
    diff = (s1 + x1) - (s2 + x2)

    if diff == 0:
        return s1 + x1 

    if diff > 0 and x2 > 0:
        return s1 + x1 

    if diff < 0 and x1 > 0:
        return s2 + x2

    return -1 
