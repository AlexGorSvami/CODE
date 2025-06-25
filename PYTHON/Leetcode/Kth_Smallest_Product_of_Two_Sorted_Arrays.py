def kthSmallestProduct(nums1:list, nums2: list, k: int) -> int:
    n,m = len(nums1), len(nums2)
    a1, a2 = [-i for i in nums1 if i < 0][::-1], [i for i in nums1 if i >= 0]
    b1, b2 = [-i for i in nums2 if i < 0][::-1], [i for i in nums2 if i >= 0]

    negative = len(a1) * len(b2) + len(a2) * len(b1)
    if k > negative:
        k -= negative
        s = 1 
    else:
        k = negative - k + 1 
        b1, b2 = b2, b1 
        s = -1

    def cnt(nums1, nums2, x):
        result = 0 
        j = len(nums2)-1
        for i in range(len(nums1)):
            while j >= 0 and nums1[i] * nums2[j] > x:
                j -= 1 
            result += j+1 
        return result 

    left, right = 0, 10**10
    while left < right:
        middle = (left + right) // 2 
        if cnt(a1, b1, middle) + cnt(a2, b2, middle) >= k:
            right = middle 
        else:
            left = middle + 1 
    return left * s 
