def maxFrequencyElements(nums: list) -> int:
    dictionary = dict(Counter(nums))
    max_dig = max(dictionary.values())
    result = 0
    for k, v in dictionary.items():
        if v == max_dig:
            result += v 
    return result 
