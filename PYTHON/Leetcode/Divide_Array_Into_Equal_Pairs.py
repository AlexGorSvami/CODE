def divideArray(nums: list) -> bool:
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0)+1

    for count in counts.values():
        if count % 2 != 0:
            return False

    return True

print(divideArray([3,2,3,2,2,2]))
print(divideArray([1,2,3,4]))
