def maximumTripletValue(nums: list) -> int:
    n = len(nums)
    max_triple_value = 0
    max_seen = 0
    max_defference = 0

    for i in range(n):
        max_triple_value = max(max_triple_value, max_defference * nums[i])
        max_defference = max(max_defference, max_seen - nums[i])
        max_seen = max(max_seen, nums[i])

    return max_triple_value 


print(maximumTripletValue([12,6,1,2,7]))
print(maximumTripletValue([1,10,3,4,19]))
print(maximumTripletValue([1,2,3]))
