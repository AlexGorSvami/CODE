from typing import List 
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = '123456789'
        result = []
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(10 - length):
                num = int(sample[start: start + length])
                if low <= num <= high:
                    result.append(num)
        return sorted(result)
