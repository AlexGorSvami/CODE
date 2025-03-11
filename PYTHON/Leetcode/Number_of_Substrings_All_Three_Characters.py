def numberOfSubstrings(s: str) -> int:
    left = 0
    chars = {'a':0, 'b':0, 'c':0}
    result = 0
    n = len(s)

    for right in range(n):
        chars[s[right]] += 1

        while all(chars.values()):
            result += n-right 
            chars[s[left]] -= 1
            left += 1 

    return result 

print(numberOfSubstrings('abcabc'))
print(numberOfSubstrings('aaacb'))
print(numberOfSubstrings('abc'))
