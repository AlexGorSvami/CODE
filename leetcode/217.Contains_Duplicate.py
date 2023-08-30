class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

class Solution1:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = {}
        for i in nums:
            if i in seen and seen[i] >= 1:
                return True
            seen[i] = seen.get(i,0)+1
        return False


