def makeLargestSpecial(s: str) -> str:
    n = len(s)
    one, zero, i = 0, 0, 0 
    build = []
    for j in range(n):
        if s[j] == '1': one += 1
        else: zero += 1
        if one == zero:
            build.append('1' + makeLargestSpecial(s[i+1:j]) + '0')
            i = j + 1
    build.sort(reverse=True)
    return ''.join(build)

