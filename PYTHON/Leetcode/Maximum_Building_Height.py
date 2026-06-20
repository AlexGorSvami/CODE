from typing import List 
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()

        for i in range(1, len(restrictions)):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + restrictions[i][0] - restrictions[i-1][0])

        for i in range(len(restrictions) - 2, -1, -1):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + restrictions[i+1][0] - restrictions[i][0])
        answer = 0 
        for i in range(1, len(restrictions)):
            id1, h1 = restrictions[i-1]
            id2, h2 = restrictions[i]
            answer = max(answer, (h1 + h2 + id2 - id1) // 2) 
            
        return max(answer, restrictions[-1][1] + n - restrictions[-1][0])
