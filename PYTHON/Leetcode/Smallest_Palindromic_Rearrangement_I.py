from collections import Counter
class Solution:
    def smallestPalindromic(self, s: str) -> str:
        cnt = Counter(s)
        left = ''.join(char * (cnt[char] // 2) for char in sorted(cnt.keys()))
        middle = ''.join(char for char in cnt if cnt[char] % 2 != 0)

        return left + middle + left[::-1]
