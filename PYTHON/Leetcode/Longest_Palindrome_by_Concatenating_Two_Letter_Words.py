def longestPalindrome(words: list) -> int:
    count = 0
    availible = {}
    two_character_palindrome = 0

    for word in words:
        rever = word[::-1]

        if rever in availible:
            count += 4
            availible[rever] -= 1

            if availible[rever] == 0:
                del availible[rever]

            if word[0] == word[1]:
                two_character_palindrome -= 1 
        
        else:
            if word in availible:
                availible[word] += 1 
            else:
                availible[word] = 1 

            if word[0] == word[1]:
                two_character_palindrome += 1 

    if two_character_palindrome > 0:
        count += 2 
    return count 


