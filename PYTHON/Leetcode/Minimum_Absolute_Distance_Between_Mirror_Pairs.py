class Solution:
    def get_mirror(self, i: int) -> int:
        out = 0 
        while i:
            out = out * 10 + i % 10
            i //= 10 
        return out 

    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)
        seen = defaultdict(int)
        diff = -1 
        for i in range(n):
            if nums[i] in seen:
                curr = i - seen[nums[i]]
                if diff == -1 or diff > curr:
                    diff = curr 
            seen[self.get_mirror(nums[i])] = i 
        return diff 


