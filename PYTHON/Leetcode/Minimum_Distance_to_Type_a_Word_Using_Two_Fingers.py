def minimumDistance(word: str) -> int:
    inf = float('inf')
    def dist(t: int, f: int) -> int:
        if f == -1:
            return 0 
        return abs(t // 6 - f // 6) + abs(t % 6 - f % 6)

    dp = {(-1, -1):0}
    for i in word:
        new_dp = {}
        j = ord(i) - ord('A')
        for k, l in dp.keys():
            new_dp[k,j] = min(new_dp.get((k,j), inf), dp[k,l] + dist(j,l))
            new_dp[j,l] = min(new_dp.get((j,l), inf), dp[k,l] + dist(j,k))
        dp = new_dp 

    return min(dp.values())
