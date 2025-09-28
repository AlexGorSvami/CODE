def largestPerimeter(nums: list) -> int:
    def valid(a, b, c):
        return a+b > c and a+c > b and b+c > a 
    nums.sort(reverse=True)
    for a, b, c in zip(nums, nums[1:], nums[2:]):
        if valid(a, b, c):
            return a + b + c
    return 0 
