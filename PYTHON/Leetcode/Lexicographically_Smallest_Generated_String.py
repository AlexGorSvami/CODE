def generateString(str1: str, str2: str) -> str:
    n1, n2 = len(str1), len(str2)
    l = n1 + n2 - 1 
    word = [None] * l 

    for i in range(n1):
        if str1[i] == 'T':
            for j in range(n2):
                position = i + j 
                if word[position] is not None and word[position] != str2[j]:
                    return ''
                word[position] = str2[j]

    free = [False] * l 
    for i in range(l):
        if word[i] is None:
            word[i] = 'a'
            free[i] = True 

    def interval_equal(i: int) -> bool:
        for j in range(n2):
            if word[i+j] != str2[j]:
                return False 
        return True 

    for i in range(n1):
        if str1[i] == 'F':
            if interval_equal(i):
                fixed = False 
                for j in range(n2-1, -1, -1):
                    position = i + j 
                    if free[position]:
                        word[position] = 'b'
                        free[position] = False 
                        fixed = True 
                        break 
                    if not fixed:
                        return ''

    return ''.join(word)

