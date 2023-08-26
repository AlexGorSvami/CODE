class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x).isdigit() and str(x) == str(x)[::-1]:
            return True
        return False
