def findNumbers(nums: list) -> int:
    return sum([1 if len(str(i)) % 2 == 0 else 0 for i in nums])


print(findNumbers([12,345, 2, 6, 7896]))
