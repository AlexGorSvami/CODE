def doesAleceWin(s: str) -> bool:
    vowels = ['a', 'e', 'i', 'o', 'u']
    if all(i not in s for i in vowels):
        return False
    return True 
