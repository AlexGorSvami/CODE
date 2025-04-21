def numberOfArrays(differences: list, lower: int, upper: int) -> int:
    min_summ = max_summ = curr = 0
    for diff in differences:
        curr += diff 
        min_summ = min(min_summ, curr)
        max_summ = max(max_summ, curr)

    return max(0, (upper - max_summ) - (lower - min_summ) + 1)



print(numberOfArrays([1,-3,4], 1, 6))
