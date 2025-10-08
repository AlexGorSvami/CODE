def successfulPairs(spells: list, potions: list, success: int) -> list:
    n = len(potions)
    potions.sort()
    result = []

    for spell in spells:
        h = n - 1
        l = 0
        while l <= h:
            middle = (h + l) // 2 
            if (potions[middle] * spell) >= success:
                h = middle - 1 
            else:
                l = middle + 1 
        result.append(n - l)

    return result 
