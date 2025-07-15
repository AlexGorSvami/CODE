def isValid(word: str) -> bool:
    vowels = constants = 0

    if len(word) < 3:
        return False 

    for w in word:
        if not w.isalnum():
            return False 

    for w in word.lower():
        if w in 'aeiou':
            vowels += 1 
        if w in 'bcdfghjklmnpqrstvwxyz':
            constants += 1 
    return vowels >= 1 and constants >= 1
