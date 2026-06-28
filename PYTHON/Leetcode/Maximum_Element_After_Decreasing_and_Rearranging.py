class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        res = 1 
        for a in arr[1:]:
            res = min(res + 1, a)
        return res 
