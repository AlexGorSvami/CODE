class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = max(1, c[1] - (c[1] % 2 == 0))
        for x in c:
            if x == 1:
                continue 
            l, v = 0, x 
            while c[v] > 1:
                l += 2 
                v *= v 
            res = max(res, l + (1 if c[v] else -1))
        return res 
