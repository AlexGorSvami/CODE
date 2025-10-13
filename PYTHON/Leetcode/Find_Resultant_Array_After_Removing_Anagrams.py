def removeAnagrams(words: list) -> list:
    stack = []
    for word in words:
        if not stack:
            stack.append(word)
        else:
            top = ''.join(sorted(stack[-1]))
            sorted_word = ''.join(sorted(word))
            if top != sorted_word:
                stack.append(word)
    return stack 
