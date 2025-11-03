def minCost(colors: str, neededTime: list) -> int:
    i, result = 0, 0
    while i < len(colors):
        s, m, j = neededTime[i], neededTime[i], i + 1 
        while j < len(colors) and colors[j] == colors[i]:
            s, m = s + neededTime[j], max(m, neededTime[j])
            j += 1 
        if j > i + 1:
            result += s - m 
            i = j 
        else:
            i += 1 
    return result 
