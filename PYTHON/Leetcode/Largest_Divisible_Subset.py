def largestDivisibleSubset(nums: list) -> list:
    max_to_set = {-1: set()}
    nums.sort()

    for num in nums:
        num_set = set()

        for max_in, i in max_to_set.items():
            if num % max_in == 0 and len(i) > len(num_set):
                num_set = i 

        max_to_set[num] = num_set | {num}

    return list(max(max_to_set.values(), key = len))


print(largestDivisibleSubset([1,2,3]))
print(largestDivisibleSubset([1,2,4,8]))
