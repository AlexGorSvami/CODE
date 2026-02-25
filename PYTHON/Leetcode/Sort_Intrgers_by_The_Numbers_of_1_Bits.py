def sortByBits(arr: list) -> list:
    def dp(n: int):
        result = 0
        while n:
            n &= n-1
            result += 1 
        return result
    arr.sort(key=lambda i: (dp(i), i))
    return arr 
