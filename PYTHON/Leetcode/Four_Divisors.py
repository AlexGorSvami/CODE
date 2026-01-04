def sumFourDivisors(nums: list) -> int:
    
    def get_divisor(n: int):
        div = 2
        div_cnt = 2
        div_sum = n + 1 

        while div <= n // div:
            if n % div == 0:
                div_cnt += 1
                div_sum += div 

                if div * div != n:
                    div_cnt += 1 
                    div_sum += n // div 

            div += 1 

        return div_sum if div_cnt == 4 else 0

    return sum(get_divisor(n) for n in nums)

