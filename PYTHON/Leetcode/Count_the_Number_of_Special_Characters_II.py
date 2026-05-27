from typing import List 
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
       last_lower = {}
       first_upper = {}

       for i, char in enumerate(word):
           if char.islower():
               last_lower[char] = i 
           elif char.isupper():
                if char not in first_upper:
                    first_upper[char] = i 

       spec_cnt = 0

       for lower_char, last_ind in last_lower.items():
            upper_char = lower_char.upper()
            if upper_char in first_upper and last_ind < first_upper[upper_char]:
                spec_cnt += 1 
       return spec_cnt 
