from typing import List 
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum, right_sum = 0, sum(nums)
        answer = []
        for n in nums:
            right_sum -= n 
            answer.append(abs(left_sum - right_sum))
            left_sum += n 
        return answer 
