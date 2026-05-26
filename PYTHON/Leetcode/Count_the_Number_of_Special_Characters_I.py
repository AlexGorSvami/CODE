class Solution: 
    def numberOfSpecialChars(self, word: str) -> int:
        lowers = set(i for i in word if word.islower())
        uppers = set(i.lower() for i in word if word.isupper())
        return len(lowers & uppers)
