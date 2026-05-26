class Solution: 
    def numberOfSpecialChars(self, word: str) -> int:
        lowers = set(i for i in word.lower())
        uppers = set(i for i in word.upper())
        return len(lowers & uppers)
