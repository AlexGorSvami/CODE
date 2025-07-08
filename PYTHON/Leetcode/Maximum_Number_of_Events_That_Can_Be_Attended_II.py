def maxValue(events: list, k: int) -> int:
    events.sort(key=lambda x: x[1])
    dp = [[0,0]]
    dp2 = [[0,0]]
    for i in range(k):
        for s,e,v in events:
            x = bisect.bisect(dp, [s])-1
            if dp[x][1]+v > dp2[-1][1]:
                dp2.append([e,dp[x][1]+v])

        dp = dp2 
        dp2 = [[0,0]]

    return dp[-1][-1]
