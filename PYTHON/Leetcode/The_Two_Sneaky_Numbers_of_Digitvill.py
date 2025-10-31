def getSneakyNumber(nums: list) -> list:
    from collections import Counter
    result = []
    cnt_numbers = Counter(nums)
    for key, value in cnt_numbers.items():
        if value >= 2:
            result.append(key)
    return result 
