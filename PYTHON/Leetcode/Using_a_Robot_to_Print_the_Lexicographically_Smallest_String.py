def robotWithString(s: str) -> str:
    n = len(s)
    minS = [None]*n 
    minS[-1] = s[-1]
    for i in range(n-2, -1, -1):
        minS[i] = min(minS[i+1], s[i])

    stack = []
    result = []
    for i in range(n):
        stack.append(s[i])
        while stack and (i == n-1 or stack[-1] <= minS[i+1]):
            result.append(stack.pop())

    return ''.join(result)
