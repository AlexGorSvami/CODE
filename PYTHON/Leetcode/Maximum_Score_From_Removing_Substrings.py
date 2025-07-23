def maximumGain(s: str, x: int, y: int) -> int:

    def remove_pair(pair, score):
        nonlocal s 
        result = 0
        stack = []
        for c in s:
            if c == pair[1] and stack and stack[-1] == pair[0]:
                stack.pop()
                result += score 
            else:
                stack.append(c)
        s = ''.join(stack)
        return result 

    result = 0 
    pair = 'ab' if x > y else 'ba'
    result += remove_pair(pair, max(x, y))
    result += remove_pair(pair[::-1], min(x, y))
    return result 
