def shortestCommonSupersequence(str1: str, str2: str) -> str:
    def get_lcs(str1, str2):
        res = []

        dp = [['' for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    dp[i+1][j+1] = dp[i][j] + str1[i]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1], key=len)
        
        return dp[-1][-1]
    lcs = get_lcs(str1, str2) 

    result = []
    i,j = 0, 0 
    for c in lcs:
        while c != str1[i]:
            result.append(str1[i])
            i += 1 

        while c != str2[j]:
            result.append(str2[j])
            j += 1 

        result.append(c)
        i += 1 
        j += 1 

    return ''.join(result) + str1[i:] + str2[j:]


print(shortestCommonSupersequence('abac', 'cab'))
print(shortestCommonSupersequence('aaaaaaaa', 'aaaaaaaa'))
