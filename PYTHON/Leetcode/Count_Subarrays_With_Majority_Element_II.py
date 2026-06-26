class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1 
        s = smaller_cnt = answer = 0 
        for num in nums:
            if num == target:
                smaller_cnt += cnt[s]
                s += 1 
            else:
                s -= 1 
                smaller_cnt -= cnt[s]

        answer += smaller_cnt 
        cnt[s] += 1 

        return answer 
