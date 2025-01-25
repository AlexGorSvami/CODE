def lexicographicallySmallestArray(nums: list, limit: int) -> list:
    length = len(nums)
    sorted_nums = sorted(zip(nums, range(length)))

    result = [0] * length 

    i = 0 
    while i < length:
        j = i + 1

        while j < length and sorted_nums[j][0] - sorted_nums[j - 1][0] <= limit:
            j += 1

        indices = sorted(index for _, index in sorted_nums[i:j])

        for sorted_index, (value, _) in zip(indices, sorted_nums[i:j]):
            result[sorted_index] = value

        i = j

    return result 


print(lexicographicallySmallestArray([1,5,3,9,8], 2))
print(lexicographicallySmallestArray([1,7,6,18,2,1], 3))
print(lexicographicallySmallestArray([1,7,28,19,10], 3))
