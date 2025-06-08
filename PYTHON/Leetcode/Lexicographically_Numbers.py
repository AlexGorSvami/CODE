def lexicalOrder(n: int) -> list:
    res = []
    stack = [1]
    while stack:
        x = stack.pop()
        res.append(x)
        if x < n and x % 10 < 9:
            stack.append(x+1)
        if x * 10 <= n:
            stack.append(x * 10)
    return res  
