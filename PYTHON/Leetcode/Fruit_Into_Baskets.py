def totalFruit(fruits: list) -> int:
    k = 2
    left = 0 
    counter = collections.Counter()
    result = 0

    for right in range(len(fruits)):
        if counter[fruits[right]] == 0:
            k -= 1 
        counter[fruits[right]] += 1 
        while k == -1:
            counter[fruits[left]] -= 1 
            if counter[fruits[left]] == 0:
                k += 1 
            left += 1 
        result = max(result, right - left + 1)
    return result 
