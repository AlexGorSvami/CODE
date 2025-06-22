def divideString(s: str, k: int, fill: str) -> list:
    while len(s) % k:
        s += fill 
    answer = []
    for i in range(0, len(s), k):
        answer.append(s[i:i+k])
    return answer 
