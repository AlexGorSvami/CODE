def canBeTypeWords(text: str, brokenLetters: str) -> int:
    split_text = text.split()
    t = [1] * len(split_text)
    for i in brokenLetters:
        for j in range(len(split_text)):
            if i in split_text[j]:
                t[j] = 0 
    return sum(t)
