def answerString(word: str, numFriends: int) -> str:
    if numFriends == 1:
        return word 

    n = len(word)
    max_split = n - numFriends+1
    result = word[:max_split]
    for i in range(n):
        result = max(result, word[i:min(n, i+max_split)])
    return result 
