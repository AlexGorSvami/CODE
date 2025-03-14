def maximumCandies(candies: list, k: int) -> int:
    totalCandies = sum(candies)

    if totalCandies < k:
        return 0

    l,r = 1, totalCandies // k
    maximum_candies = 0

    while l <= r:
        m = (l + r) // 2 
        divide_candy = 0

        for candy in candies:
            if candy >= m:
                divide_candy += candy // m 

            if divide_candy >= k:
                break 
        if divide_candy >= k:
            maximum_candies = m 
            l = m + 1 
        else:
            r = m - 1 
    return maximum_candies


print(maximumCandies([5,8,6], 3))
print(maximumCandies([2,5], 11))

