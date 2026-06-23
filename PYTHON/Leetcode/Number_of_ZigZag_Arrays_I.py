class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        k = r - l + 1 
        if n == 1:
            return max(0, k)
        if k < 2:
            return 0 

        MOD = 10**9 + 7 
        up, down = [1] * k, [1] * k 

        for _ in range(n - 1):
            n_up, n_down = [0] * k, [0] * k 
            s_down, s_up = 0, 0 
            for i in range(1, k):
                s_down = (s_down + down[i-1]) % MOD 
                n_up[i] = s_down 

                s_up = (s_up + up[k-i]) % MOD 
                n_down[k - i - 1] = s_up 
            up, down = n_up, n_down 

        return (sum(up) + sum(down)) % MOD 
