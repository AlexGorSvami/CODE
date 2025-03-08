def minimumRecolors(blocks: str, k:int) -> int:
    n = len(blocks)
    black = 0
    cnt = 0
    for i in range(n):
        if blocks[i] == 'B':
            cnt += 1

        if i >= k-1:
            black = max(black, cnt)
            if blocks[i-k+1] == 'B':
                cnt -= 1 
    return k-black 



print(minimumRecolors('WBBWWBBWBW', 7))
print(minimumRecolors('WBWBBBW', 2))
