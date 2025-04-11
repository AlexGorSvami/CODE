def countSymmetricIntegers(low: int, high: int) -> int:
    n = 0

    for i in range(low, high+1):
        s = str(i)
        length = len(s)
        if length % 2 == 0:
            length1 = length // 2
            s1 = s[:length1]; ss1 = 0
            s2 = s[length1:]; ss2 = 0 
            for j in range(length1):
                ss1 = ss1 + int(s1[j])
                ss2 = ss2 + int(s2[j])
            if ss1 == ss2:
                n = n+1 
    return n

print(countSymmetricIntegers(1,100))
print(countSymmetricIntegers(1200, 1230))
