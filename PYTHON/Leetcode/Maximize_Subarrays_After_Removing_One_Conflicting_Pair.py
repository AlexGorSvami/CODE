def maxSubarrays(n: int, conflictingPairs: list) -> int:
    valid_subarrays = 0
    max_left = 0
    second_max_left = 0 
    gains = [0] * (n + 1)
    conflicts = [[] for _ in range(n + 1)]

    for i, j in conflictingPairs:
        conflicts[max(i, j)].append(min(i, j))

    for right in range(1, n+1):
        for left in conflicts[right]:
            if left > max_left:
                second_max_left = max_left 
                max_left = left 
            elif left > second_max_left:
                second_max_left = left 

        valid_subarrays += right - max_left 
        gains[max_left] += max_left - second_max_left 

    return valid_subarrays + max(gains)
    
