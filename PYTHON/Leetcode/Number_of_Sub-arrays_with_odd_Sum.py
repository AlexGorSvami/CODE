def numOfSubarrays(arr: list) -> int:
    mod = 10**9 + 7
    even = 1
    odd = 0
    curr_summ = 0
    soln = 0
    for num in arr:
        curr_summ += num 
        if curr_summ % 2:
            soln = (soln + even) % mod 
            odd = (odd + 1) % mod 
        else:
            soln = (soln + odd) % mod 
            even = (even + 1) % mod 
    return soln % mod 


print(numOfSubarrays([1,3,5]))
print(numOfSubarrays([2,4,6]))
print(numOfSubarrays([1,2,3,4,5,6,7]))

