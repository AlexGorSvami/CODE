from typing import List 
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        answer = 0
        n = len(colors)
        for i in range(n):
            if colors[0] != colors[i]:
                answer = max(answer, i)
            if colors[i] != colors[-1]:
                answer = max(answer, n - 1 - i)
        return answer 
    
