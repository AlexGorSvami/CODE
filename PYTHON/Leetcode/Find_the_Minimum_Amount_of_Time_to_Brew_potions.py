def minTime(skill: list, mana: list) -> int:
    n, m = len(skill), len(mana)
    times = [0] * n

    for i in range(m):
        curr = 0 
        for j in range(n):
            curr = max(curr, times[j]) + skill[j] * mana[i]
        times[n-1] = curr

        for k in range(n-2, -1, -1):
            times[k] = times[k+1] - skill[k+1] * mana[i]

    return times[-1]
