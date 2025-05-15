def getLongestSubsequence(words: list, groups: list) -> list:
    answer = []
    prev = -1 
    for i in range(len(words)):
        if groups[i] != prev:
            answer.append(words[i])
            prev = groups[i]
        elif len(words[i]) > len(answer[-1]):
            answer[-1] = words[i]

    return answer 
