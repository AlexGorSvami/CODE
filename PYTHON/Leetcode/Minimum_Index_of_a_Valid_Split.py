def minimumIndex(nums: list) -> int:
    n = len(nums)
    cnt = Counter(nums)
    def_dic = defaultdict(int)

    for i in range(len(nums)):
        def_dic[nums[i]] += 1 
        if (cnt[nums[i]] - def_dic[nums[i]])*2 > n-(i+1) and def_dic[nums[i]]*2 > i+1:
            return 1 
    
    return -1


print(minimumIndex([1,2,2,2]))
print(minimumIndex([2,1,3,1,1,1,7,1,2,1]))
