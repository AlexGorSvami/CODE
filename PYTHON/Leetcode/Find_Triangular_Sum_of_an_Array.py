def triangularSum(nums: list) -> int:
    return sum(x*comb(len(nums)-1,i)for i,x in enumerate(nums)) % 10
