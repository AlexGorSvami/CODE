def triangleType(nums: list) -> str:
    nums.sort()
    a, b, c = nums
    if a + b <= c:
        return 'none'
    if a == b == c:
        return 'equilateral'
    if a == b or b == c:
        return 'isosceles'
    return 'scalene'


print(triangleType([3,3,3]))
print(triangleType([3,4,5]))
