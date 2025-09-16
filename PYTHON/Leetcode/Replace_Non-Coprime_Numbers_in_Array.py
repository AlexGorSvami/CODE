def replaceNonCoprimes(nums: list) -> list:
    def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

    stack = []
    for num in nums:
        while stack:
            g = gcd(stack[-1], num)
            if g > 1:
                num = stack.pop() * num // g
            else:
                break
        stack.append(num)
    return stack
