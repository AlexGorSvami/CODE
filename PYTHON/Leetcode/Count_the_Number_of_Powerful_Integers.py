def numberOfPowerfulInt(start: int, finish: int, limit: int, s: str) -> int:
   
    def count(x):

         def length(x):
            res = 0
            while x:
                x //= 10
                res += 1
            return res 
        
        res = 0
        n = length(x)
        base = 10**n 
        l = n - len(s)
        count = (limit+1) ** l 
        for i in range(l):
            base //= 10
            curr = x // base%10 
            count //= limit + 1
            res += (min(curr-1, limit)-0+1)*count 
            if curr > limit:
                break 

        else:
            if x % base >= int(s):
                res += 1 
        return res 
    
    return count(finish) - count(start-1)



