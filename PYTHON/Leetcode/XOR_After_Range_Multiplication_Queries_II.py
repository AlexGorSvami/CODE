import collections
from functools import reduce

class Solution:
    def xorAfterQueries(self, nums: list, queries: list) -> int:
        MOD = 10 ** 9 + 7 
        
        def dfs(x):
            return pow(x, MOD - 2, MOD)

        size = int(len(nums) ** 0.5) + 1 
        diff = collections.defaultdict(lambda: [1] * len(nums))
        
        for i, j, k, l in queries:
            if k <= size:
                diff[k][i] = (diff[k][i] * l) % MOD 
                j += k - (j - i) % k 
                if j < len(nums):
                    diff[k][j] = (diff[k][j] * dfs(l)) % MOD 
            else:
                for m in range(i, j + 1, k):
                    nums[m] = (nums[m] * l) % MOD
                    
        for k, dif in diff.items():
            for i in range(len(dif)):
                if i - k >= 0:
                    dif[i] = (dif[i] * dif[i - k]) % MOD 
                nums[i] = (nums[i] * dif[i]) % MOD 
                
        return reduce(lambda a, x: a ^ x, nums, 0)
