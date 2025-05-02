def pushDominoes(dominoes: str) -> str:
        N = len(dominoes)
        l = -1
        r = -1
        res = list(dominoes)        

        for i in range(N + 1):
            if i == N or res[i] == 'R':
                if r > l:   
                    # R...R, turn all to R
                    while r < i:
                        res[r] = 'R'
                        r += 1
                # else: r < l, L...R, do nothing
                r = i
            elif res[i] == 'L':
                if l > r or r == -1:
                    # L...L, turn all to L
                    while l < i - 1:
                        l += 1
                        res[l] = 'L'
                    # Now l = i - 1

                else:  # R...L, turn until lo = hi
                    l = i  # move l directly to i
                    lo = r + 1
                    hi = l - 1
                    while lo < hi:  # Note "<" not "<=" because "R.L" is the final state
                        res[lo] = 'R'
                        res[hi] = 'L'
                        lo += 1
                        hi -= 1
        
        return ''.join(res)



print(pushDominoes('RR.L'))
print(pushDominoes('L.R...LR..L..'))
