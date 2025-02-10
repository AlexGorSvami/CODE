def clearDigits(s: str) -> str:
    stack = []
    for ch in s:
        if ch.isdigit():
            stack.pop()
        else:
            stack.append(ch)
    
    return ''.join(stack)


print(clearDigits('abc'))
print(clearDigits('cb34'))
