from typing import List 
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []

        for q in queries:
            for word in dictionary:
                cnt = 0 
                for i in range(len(q)):
                    if q[i] != word[i]:
                        cnt += 1 
                    if cnt > 2:
                        break 

                if cnt <= 2:
                    result.append(q)
                    break 

        return result

