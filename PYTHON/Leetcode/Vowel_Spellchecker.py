def spellcheker(wordlist: list, queries: list) -> list:
    def fix_vowels(words):
        return reduce(lambda w, v: w.replace(v, '_'), 'aeiou', words.lower())

    dict_exact, dict_case, dict_vowels = set(wordlist), {}, {}
    for word in wordlist:
        dict_case.setdefault(word.lower(), word)
        dict_vowels.setdefault(fix_vowels(word), word)
    result = []
    for query in queries:
        if query in dict_exact:
            result.append(query)
        else:
            result.append(dict_case.get(query.lower(), dict_vowels.get(fix_vowels(query),'')))
    return result 
