def countandsay(n: int) -> str:
    if n == 1:
        return "1"
    else:
        return read(countandsay(n-1))

def read(num):
    p = num[0]
    count = 0
    out = ''
    for i in num:
        if i == p:
            count += 1 
        else:
            out += str(count) + p
            count = 1 
            p = i 
    out += str(count) + p 
    return out 

print(countandsay(4))
print(countandsay(1))

