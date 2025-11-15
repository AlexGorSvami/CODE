def numberOfSubstrings(s: str) -> int:
    result = 0
    values = [-1]
    for key, value in enumerate(s):
        ones = zeros = 0 
        if value == '1':
            ones += 1 
        else:
            zeros += 1 
        p = key 
        for k in values[::-1]:
            ones += p - k - 1 
            result += max(0, min(p - k, ones - zeros ** 2 + 1))
            p = k 
            zeros += 1 
            if zeros ** 2 > key:
                break
        if value == '0':
            values.append(key)

    return result 
