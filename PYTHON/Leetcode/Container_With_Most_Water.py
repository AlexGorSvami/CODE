def maxArea(height: list) -> int:
    result = 0 
    n = len(height)
    l, r = 0, n-1

    while l < r:
        area = min(height[l], height[r]) * (r - l) 
        result = max(result, area)

        if height[l] < height[r]:
            l += 1 
        else:
            r -= 1 
    return result 
