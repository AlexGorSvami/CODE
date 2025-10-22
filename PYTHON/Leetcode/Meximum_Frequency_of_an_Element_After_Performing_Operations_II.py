def maxFrequency(nums: list, k: int, numOperations: int) -> int:
    n = len(nums)
    max_el = max(nums)
    mp = defaultdict(int)
    frequency = defaultdict(int)
    answer = 1 
    cum_sum = 0 

    for n in nums:
        frequency[n] += 1 
        l = max(n - k, 0)
        r = min(n + k, max_el + k)
        mp[l] += 1 
        mp[r + 1] -= 1 
        mp[n] += 0 

    for key in sorted(mp.keys()):
        mp[key] += cum_sum 
        cum_sum = mp[key]
        target = key 
        target_frequency = frequency[target]
        need_conversion = mp[target] - target_frequency 
        max_poss_conversion = min(need_conversion, numOperations)
        answer = max(answer, target_frequency + max_poss_conversion)

    return answer 
