def kthCharacter(k: int, operations: list) -> str:
    if k == 1:
        return 'a'
    l = 1
    shift = 0
    ind = 0

    while l < k:
        l <<= 1 
        ind += 1 

    ind -= 1

    while k > 1:
        next = l >> 1
        off = l - k 
        if off < next:
            k = next - off 
            shift = (shift + operations[ind]) % 26
        l = next 
        ind -= 1 

    return chr(ord('a') + shift)
