def maximizeSquareHoleArea(n: int, m: int, hBars: list, vBars:list) -> int:
    def helper(nums: list):
        cnt, answer = 1, 1 
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                cnt += 1 
            else:
                cnt = 1
            answer = max(answer, cnt)
        return answer 

    answer = min(helper(hBars), helper(vBars))
    return (answer + 1) ** 2
        

        

