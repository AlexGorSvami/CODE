def maxSumTronic(nums: list) -> int:
    n = len(nums)
    dec_len = [1] * n 
    dec = nums.copy()
    for i in range(1, n):
        if nums[i] < nums[i-1]:
            dec_len[i] = dec_len[i-1] + 1 
        dec[i] += dec[i-1]

    inc = nums.copy()
    for i in range(1, n):
        if nums[i] > nums[i-1]:
            inc[i] += max(0, inc[i-1])

    rev_inc = nums.copy()
    for i in range(n-2, -1, -1):
        if nums[i+1] > nums[i]:
            rev_inc[i] += max(0, rev_inc[i+1])

    answer = -inf 
    for i in range(1, n-1):
        if nums[i] >= nums[i+1] or dec_len[i] <= 1:
            continue 
        j = i - dec_len[i] + 1
        if j == 0 or nums[j-1] >= nums[j]:
            continue 
        curr = inc[j-1] + dec[i] + rev_inc[i+1]
        answer = max(answer, curr)

    return answer

