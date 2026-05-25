from typing import List 
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q, mx = [0], 0 
        for i in q:
            if i == len(s) - 1: 
                return True 
            for j in range(max(i + minJump, mx), min(i + maxJump + 1, len(s))):
                if s[j] == '0':
                    q.append(j)
            mx = max(mx, i + maxJump + 1)
        return False
