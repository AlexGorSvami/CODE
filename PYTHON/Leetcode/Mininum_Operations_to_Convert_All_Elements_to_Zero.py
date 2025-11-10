def minOperations(nums: list) -> int:
    stack, result = [], 0
    for num in nums:
        while stack and stack[-1] > num:
            stack.pop()
        if num == 0:
            continue 
        if not stack or stack[-1] < num:
            result += 1 
            stack.append(num)
    
    return result 
