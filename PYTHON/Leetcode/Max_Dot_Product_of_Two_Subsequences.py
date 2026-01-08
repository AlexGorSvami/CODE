def maxDotProduct(nums1: list, nums2: list) -> int:
    nums1 = [-1000] + nums1
    nums2 = [-1000] + nums2
    len_nums1 = len(nums1)
    len_nums2 = len(nums2)
    dp = [([-10**7] * len_nums2) for _ in range(len_nums1)]

    for i in range(1, len_nums1):
        for j in range(1, len_nums2):
            dp[i][j] = nums1[i] * nums2[j] + max(0, dp[i-1][j-1])
            dp[i][j] = max([dp[i][j], dp[i-1][j], dp[i][j-1]])

    return dp[-1][-1]
