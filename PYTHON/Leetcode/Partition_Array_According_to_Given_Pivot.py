def pivotArray(nums: list, pivot: int) -> list:
    result = [None] * len(nums)
    low, high = 0, len(nums) - 1
    for i in nums:
        if i < pivot:
            result[low] = i 
            low += 1
        elif i > pivot:
            result[high] = i 
            high -= 1 
    ind = 0
    for i, num in enumerate(result):
        if num == None:
            result[i] = pivot 
            ind = i 
    result[ind +1:] = result[ind + 1:][::-1]
    return result 



print(pivotArray([9,12,5,10,14,3,10], 10))
print(pivotArray([-3,4,3,2], 2))
