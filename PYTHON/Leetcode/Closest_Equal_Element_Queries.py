class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        distance = [n] * n
        left = {}
        for i in range(2 * n-1):
            x = nums[i%n]
            if x in left:
                distance[i%len(distance)] = min(distance[i%len(distance)], i-left[x])
            left[x] = i 
        right = {}
        for i in reversed(range(2*n-1)):
            x = nums[i%n]
            if x in right:
                distance[i%n] = min(distance[i%len(distance)], right[x]-i)
            right[x] = i 
        result = [-1] * len(queries)
        for i, x in enumerate(queries):
            if distance[x] < n:
                result[i] = distance[x]
        return result 
