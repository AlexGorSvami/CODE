def countDays(days: int, meetings: list) -> int:
    free = 0
    prev = 0

    for start, end in sorted(meetings):
        if start > prev:
            free += start - prev - 1
        prev = max(prev, end)

    return free + max(0, days - prev)

print(countDays(10, [[5,7], [1,3], [9,10]]))
print(countDays(5, [[2,4], [1,3]]))
