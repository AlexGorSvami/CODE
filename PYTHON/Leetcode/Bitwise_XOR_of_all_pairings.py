def xorAllNums(nums1: list, nums2: list) -> int:
    from functools import reduce
    import operator


    list1, list2 = len(nums1), len(nums2)
    result = 0
    if list1 & 1:
        result ^= reduce(operator.xor, nums2)
    if list2 & 1:
        result ^= reduce(lambda x, y: x ^ y, nums1)

    return result

print(xorAllNums([2,1,3], [10,2,5,0]))
print(xorAllNums([1,2], [3,4]))


