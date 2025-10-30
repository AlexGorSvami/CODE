def minNumberOperations(target: list) -> int:
    result = target[0]
    for i in range(1, len(target)):
        if target[i-1] < target[i]:
            result += abs(target[i-1] - target[i])
    return result
