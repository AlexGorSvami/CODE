def isValid(s: str) -> bool:
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()','')
        s = s.replace('[]','')
        s = s.replace('{}', '')

    return not s

s = '{[[(]]}'
print(isValid(s))

