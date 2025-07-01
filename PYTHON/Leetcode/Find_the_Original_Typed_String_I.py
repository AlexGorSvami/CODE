def possibleStringCount(word: str) -> int:
    result = 1
    for i in range(1, len(word)):
        if word[i - 1] == word[i]:
            result += 1
    return result 
