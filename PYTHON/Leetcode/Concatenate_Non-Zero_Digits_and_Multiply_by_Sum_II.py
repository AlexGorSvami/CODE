class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        C, V, S, P = [0], [0], [0], [1]
        
        for c in s:
            C.append(C[-1] + (c != '0'))
            if c != '0':
                v = int(c)
                V.append((V[-1] * 10 + v) % MOD)
                S.append(S[-1] + v)
                P.append((P[-1] * 10) % MOD)
                
        return [
            0 if (a := C[l]) == (b := C[r+1]) else 
            ((V[b] - V[a] * P[b-a]) * (S[b] - S[a])) % MOD
            for l, r in queries
        ]
