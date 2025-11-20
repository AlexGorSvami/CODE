def intersectionSizeTwo(intervals: list) -> int:
    max2 = [float('-inf')] * 2
    cnt = 0
    for lo, hi in sorted(intervals, key=lambda t:(t[1], -t[0])):
        intcnt = sum(x>=lo for x in max2)
        cnt += 2 - intcnt
        if intcnt == 0:
            max2 = hi-1, hi
        elif intcnt == 1:
            max2 = max2[1], hi
    return cnt
