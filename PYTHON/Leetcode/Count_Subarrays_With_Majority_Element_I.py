class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        answer = curr_sum = less_cnt = 0 
        freq = defaultdict(int)
        freq[0] = 1 

        for x in nums:
            if x == target:
                less_cnt += freq[curr_sum]
                curr_sum += 1 
            else:
                curr_sum -= 1 
                less_cnt -= freq[curr_sum]

            answer += less_cnt 
            freq[curr_sum] += 1 

        return answer 
