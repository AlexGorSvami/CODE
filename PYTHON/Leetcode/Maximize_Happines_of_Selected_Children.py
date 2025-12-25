def maximumHappinessSum(happines: list, k: int) -> int:
    happines.sort(reverse=True)
    i, answer = 0, 0 
    while k:
        happines[i] = max(happines[i] - i, 0)
        answer += happines[i]
        i += 1 
        k -= 1 
    return answer 
