def countOfSubsrings(word: str, k: int) -> int:
    from collections import defaultdict 
    
    def func(k):
        cnt_vowels = defaultdict(int)
        cnt_non_vowel = 0
        vowels = 'aieou'
        res = 0
        left = 0
        for right in range(len(word)):
            if word[right] in vowels:
                cnt_vowels[word[right]] += 1
            else:
                cnt_non_vowel += 1
            while len(cnt_vowels) == 5 and cnt_non_vowel >= k:
                res += (len(word) - right)
                if word[left] in vowels:
                    cnt_vowels[word[left]] -= 1 
                else:
                    cnt_non_vowel -= 1

                if cnt_vowels[word[left]] == 0:
                    cnt_vowels.pop(word[left])
                left += 1 
        return res 
    return func(k) - func(k+1)

print(countOfSubsrings('aeioqq', 1))
print(countOfSubsrings('aeiou', 0))
print(countOfSubsrings('ieaouqqieaouqq', 1))
