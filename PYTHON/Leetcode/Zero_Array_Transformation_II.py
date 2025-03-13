def minZeroArray(nums: list, queries: list) -> int:
    derive = [0] * (len(nums)+1)
    pref = k = 0
    for i in range(len(nums)):
        while pref + derive[i] < nums[i]:
            if k == len(queries):
                return -1
            l, r, val = queries[k]
            if r < i:
                k += 1 
                continue 
            derive[max(l,i)] += val 
            derive[r+1] -= val 
            k += 1
        pref += derive[i]
    return k 




print(minZeroArray([2,0,2], [[0,2,1], [0,2,1], [1,1,3]]))
print(minZeroArray([4,3,2,1], [[1,3,2], [0,2,1]]))
