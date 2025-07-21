def makeFancyString(s: str) -> str:
    count, answer = 0, []
    for i, j in enumerate(s):
        if i > 0 and j == s[i-1]:
            count += 1 
        else:
            count = 1 
        if count < 3:
            answer.append(j)
    
    return ''.join(answer)
