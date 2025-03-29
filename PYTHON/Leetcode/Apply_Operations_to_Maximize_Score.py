def maximumScore(nums: list, k: int) -> int:
    M = 10 ** 9 + 7
    n = len(nums)
    old = nums[:]
    MAX = max(nums) + 1 
    v = [False] * MAX 
    sp = [0] * MAX 

    for i in range(2, MAX, 2):
        sp[i] = 2 

    for i in range(3, MAX, 2):
        if not v[i]:
            sp[i] = i 
            j = i 
            while j * i < MAX:
                if not v[j * i]:
                    v[j * i] = True 
                    sp[j * i] = i 
                j += 2 

    for i in range(n):
        ctr = set()
        cur = nums[i]
        while cur > 1:
            ctr.add(sp[cur])
            cur //= sp[cur]
        nums[i] = len(ctr)
    prev = [-1] * n 
    nxt = [n] * n 
    stack = []
    
    for i in range(n):
        while len(stack) > 0 and nums[i] > nums[stack[-1]]:
            cur = stack.pop()
            nxt[cur] = i 
        if len(stack) > 0:
            prev[i] = stack[-1]
        stack.append(i)

    result = 1 
    nums = [(old[i], i) for i in range(n)]
    nums.sort(reverse=True)

    for val, pos in nums:
        ctr = (pos - prev[pos]) * (nxt[pos] - pos)
        ctr = min(ctr, k)
        result *= pow(val, ctr, M)
        result %= M 
        k -= ctr 
        if k <= 0:
            break 
    return result 


