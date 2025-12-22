def minDeletionSize(strs: list) -> int:
    dp = [1] * len(strs[0])
    for i in range(len(strs[0])):
        for j in range(i):
            if dp[i] < dp[j] + 1:
                for k in range(len(strs)):
                    if strs[k][j] > strs[k][i]:
                        break 
                else:
                    dp[i] = dp[j] + 1 
    
    return len(strs[0]) - max(dp)
