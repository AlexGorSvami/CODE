def tupleSameProduct(nums: list) -> int:
    from collections import defaultdict
    from math import comb

    count = 0
    n = len(nums)
    products = defaultdict(set)

    for i in range(n):
        for j in range(i+1):
            products[nums[i] * nums[j]].update({i, j})

    for subset in products.values():
        if len(subset) >= 4:
            count += 8 * (comb(len(subset) // 2, 2))

    return count 






print(tupleSameProduct([2,3,4,6]))
print(tupleSameProduct([1,2,4,5,10]))
