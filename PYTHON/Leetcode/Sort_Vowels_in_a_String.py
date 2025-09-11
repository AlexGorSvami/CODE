def sortVowels(s: str) -> str:
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    cnt_chars = Counter(s)
    s_vowels = []
    for char in cnt_chars.keys():
        if char in vowels:
            s_vowels.append(char)
            s = s.replace(char, '_')
    s_vowels.sort()
    for char in s_vowels:
        s = s.replace('_', char, cnt_chars[char])
    return s 
