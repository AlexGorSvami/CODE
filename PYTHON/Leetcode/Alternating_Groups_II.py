def numberOfAlternatingGroups(colors: list, k: int) -> int:
    n = len(colors)
    result, count = 0, 1
    for i in range(-k+2, n, 1):
        if colors[i] != colors[i-1]:
            count += 1 
        else:
            count = 1 
        if count >= k:
            result += 1 
    return result 

print(numberOfAlternatingGroups([0,1,0,1,0], 3))
print(numberOfAlternatingGroups([0,1,0,0,1,0,1], 6))
print(numberOfAlternatingGroups([1,1,0,1], 4))
