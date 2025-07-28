def count_Max_Or_Subsets(nums: list) -> int:
    max_or = 0
    for num in nums:
        max_or |= num 

    result = 0
    def dfs(i, cur):
        nonlocal result, max_or 

        if i == len(nums):
            result += 1 if cur == max_or else 0 
            return 
        dfs(i+1, cur)
        dfs(i+1, cur | nums[i])

    dfs(0, 0)
    return result 
