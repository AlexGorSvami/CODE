def findWordsContaining(words: list, x: str) -> list:
    word_cnt = []
    for pos, word in enumerate(words):
        if x in word:
            word_cnt.append(pos)
    return word_cnt 

print(findWordsContaining(['leet', 'code'], 'e'))
print(findWordsContaining(['abc', 'bcd', 'aaaa', 'cbc'], 'a'))
