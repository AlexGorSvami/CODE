def find_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1 
        right += 1 

    return right - left - 1 

def longestPalindrome(s:str) -> str:
    start = 0
    end = 0

    for i in range(len(s)):
        len1 = find_center(s, i, i)
        len2 = find_center(s, i, i+1)

        length = max(len1, len2)

        if length > end - start:
            start = i - (length - 1) // 2 
            end = i + length // 2 

    return s[start:end+1]

print(longestPalindrome('babad'))
print(longestPalindrome('cbbd'))


