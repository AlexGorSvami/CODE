def colorTheGrid(m: int, n: int) -> int:
    mod = 10**9 + 7 
    masks = []

    def generate_mask(mask, pos):
        if pos == n:
            masks.append(mask)
            return 
        for color in range(3):
            if pos == 0 or ((mask >> (2 * (pos - 1))) & 3) != color:
                generate_mask(mask | (color << (2 * pos)), pos + 1)

    generate_mask(0, 0)

    dp = [[0] * len(masks) for _ in range(m)]

    for j in range(len(masks)):
        dp[0][j] = 1 

    for i in range(1, m):
        for j in range(len(masks)):
            for k in range(len(masks)):
                if not has_conflict(masks[j], masks[k], n):
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % mod 

    res = sum(dp[m-1][j] fo j in range(len(masks))) % mod 
    return res 

def has_conflict(m1, m2, n):
    for i in range(n):
        color1 = (m1 >> (2 * i)) & 3 
        color2 = (m2 >> (2 * i)) & 3 
        if color1 == color2:
            return True 
    return False



def colorTheGrid1(m: int, n: int) -> int:
    @cache
    def helper(i, j, mask):
        if j == n:
            return 1 
        if i == m:
            return helper(0, j+1, mask)

        answer = 0
        for x in [1 << 2*i, 1 << 2*i+1, 0b11 << 2*i]:
            aux = mask ^ x 
            if aux & (0b11 << 2*i):
                if (i == 0 or (aux >> 2*i) & 0b11 != (aux >> 2*i-2) & 0b11):
                    answer += helper(i + 1, j, aux)

        return answer % MOD 

    MOD = 10**9 + 7 

    return helper(0,0,0)
