def countInterestingSubarrays(nums: list, modulo: int, k: int) -> int:
    output: int = 0
    hashmap: dict[int, int] = dict()
    hashmap[0] = 1 
    cnt: int = 0
    for i in range(len(nums)):
        if nums[i] % modulo == k: cnt += 1 
        output += hashmap.get((cnt + modulo - k) % modulo, 0)
        hashmap[cnt % modulo] = hashmap.get(cnt % modulo, 0) + 1 
    return output


print(countInterestingSubarrays([3,2,4], 2, 1))
print(countInterestingSubarrays([3,1,9,6], 3, 0))
