def duplicate_encode(word):
    word = word.lower()
    res = ''
    for i in range(len(word)):
        if word.count(word[i]) > 1:
            res += ')'
        else:
            res += '('
    return res

print(duplicate_encode('recede'))
