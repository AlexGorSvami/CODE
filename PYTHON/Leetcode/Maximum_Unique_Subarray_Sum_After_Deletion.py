def maxSum(nums: list) -> int:
    l = len(nums)
    record = {}
    max_val_record = (-101)
    max_sum_res = 0 

    for ind in range(l):
        max_val_record = max(max_val_record, nums[ind])
            
        if (nums[ind] <= 0):
            continue 
        if (nums[ind] in record):
            continue 

        record[nums[ind]] = True 
        max_sum_res += nums[ind]

    return (max_val_record if (max_val_record <= 0) else max_sum_res)
