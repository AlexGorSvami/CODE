def soupServings(n: int) -> float:
    if n >= 5000:
        return 1 

    @cache
    def prob(a_rem: int, b_rem: int) -> float:
        if a_rem <= 0:
            if b_rem <= 0:
                return 0.5 
            return 1
        if b_rem <= 0:
            return 0 
        
        return (sum(
            prob(
            a_rem - remove_a, b_rem - 100 + remove_a) 
            for remove_a in range (100, 24, -25)) * 0.25
                )

    return prob(n, n)
        
