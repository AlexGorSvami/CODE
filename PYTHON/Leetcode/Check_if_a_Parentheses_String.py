def canBeValid(s:str, locked: str) -> bool:
    if len(s) % 2 != 0:
        return False

    # Check for a valid sequence from left to right
    balance = 0
    for i in range(len(s)):
        if locked[i] == '1' and s[i] == ')':
            balance -= 1
        else:
            balance += 1

        if balance < 0:
            return False 
    #Check for a valid sequence from right to left
    balance = 0
    for i in range(len(s)-1, -1, -1):
        if locked[i] == '1' and s[i] == '(':
            balance -= 1
        else:
            balance += 1

        if balance < 0:
            return False

    return True

print(canBeValid('()()', locked = '0000'))
print(canBeValid(')', locked='0'))
print(canBeValid('))()))', locked = '010100'))
