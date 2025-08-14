def largestGoodInteger(num: str) -> str:
    for i in range(9, -1, -1):
        res = str(i)*3
        if num.find(res) >= 0:
            return res 
    return ''
