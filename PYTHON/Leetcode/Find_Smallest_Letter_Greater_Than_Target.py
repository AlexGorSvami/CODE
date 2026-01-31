def nextGreatestLetter(letters: list, target: str) -> str:
    for i in letters:
        if i > target:
            return i 
    return letters[0]

