def threeConsecutiveOdds(arr: list) -> bool:
    cnt = 0
    for a in arr:
        if a % 2 == 1:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            return True
        return False


print(threeConsecutiveOdds([2,6,4,1]))
