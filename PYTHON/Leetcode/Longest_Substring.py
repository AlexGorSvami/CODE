class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_dict = {}
        max_len = 0
        start = 0

        for end in range(len(s)):
            if s[end] in chars_dict:
                start = max(start, chars_dict[s[end]] + 1)
            chars_dict[s[end]] = end
            max_len = max(max_len, end - start + 1)

        return max_len
