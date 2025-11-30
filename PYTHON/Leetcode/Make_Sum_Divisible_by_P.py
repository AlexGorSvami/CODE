def minsubarray(nums: list, p: int) -> int:
    residual = sum(nums) % p 
    if residual == 0:
        return 0 
    sm, result = 0, float('inf')
    sm_index = {0: -1}
    for i, num in enumerate(nums):
        sm = (sm + num) % p 
        result = min(result, i - sm_index.get((sm - residual) % p, float('-inf')))
        sm_index[sm] = i 
    return -1 if result in (float('inf'), len(nums)) else result 
