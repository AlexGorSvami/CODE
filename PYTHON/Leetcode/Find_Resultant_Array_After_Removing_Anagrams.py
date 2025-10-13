def removeAnagrams(words: list) -> list:
    i, j = 0, set(words)
    while i < len(words)-1:
        if sorted(words[i]) == sorted(words[i+1]):
            j.remove(words[i+1])
        else:
            i += 1 
    return words 
