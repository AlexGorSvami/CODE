class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last, res = {'a': -1, 'b': -1, 'c': -1}, 0 
        for i, c in enumerate(s):
            last[c] = i 
            res += min(last.values()) + 1 
        return res 
