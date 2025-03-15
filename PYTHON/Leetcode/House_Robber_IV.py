def minCapibality(nums: list, k: int) -> int:
        n=len(nums)
        x0=min(nums)
        xM=max(nums)
        def f(cap):
            steal, i=0, 0
            while i<n and steal<=k:
                if nums[i]<=cap:
                    steal+=1
                    i+=1
                i+=1
            return steal>=k

        l, r=x0, xM
        while l<r:
            m=(l+r)>>1
            if f(m):
                r=m
            else:
                l=m+1
        return l


print(minCapibality([2,3,5,9], 2))
print(minCapibality([2,7,9,3,1], 2))

