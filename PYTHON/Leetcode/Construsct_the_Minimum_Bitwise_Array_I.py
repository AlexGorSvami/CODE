def minBitwiseArray(nums: list) -> list:
    answer = []
    for num in nums:
        res = -1
        n = 1 
        while (num & n):
            res = num - n 
            n <<= 1 

        answer.append(res)

    return answer 
