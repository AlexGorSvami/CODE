def maximumTotalDamage(power: list) -> int:
    cnt = defaultdict(lambda: 0)
    for i in power:
        cnt[i] += i 

    nums = sorted([i for i in cnt])
    array = [-3]
    dp = [0]
    for num in nums:
        value = num - 2 
        ind = bisect_left(array, value) - 1 
        array.append(num)
        dp.append(max(dp[-1], dp[ind] + cnt[num]))
    return max(dp)
