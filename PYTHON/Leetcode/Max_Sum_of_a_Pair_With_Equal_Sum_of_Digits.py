def maximumSum(nums: list) -> int:
    from collections import defaultdict
    from sortedcontainers import SortedList
    default_dict = defaultdict(SortedList)
    def sum(num):
        result = 0
        for i in str(num):
            result += int(i)
        return result 
    for num in nums:
        default_dict[sum(num)].add(num)
    result = -1
    for key in default_dict:
        if len(default_dict[key]) >= 2:
            result = max(result, default_dict[key][-1] + default_dict[key][-2])
    return result 



print(maximumSum([18, 43, 36, 13, 7]))
print(maximumSum([10, 12, 19, 14]))
