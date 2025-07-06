from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: list, nums2: list):
        self.nums1 = nums1 
        self.nums2 = nums2 
        self.counter = Counter(nums2)

    def add(self, index: int, value: int) -> None:
        num = self.nums2[index]
        self.counter[num] -= 1 
        if self.counter[num] == 0:
            del self.counter[num]
        self.nums2[index] += value
        self.counter[self.nums2[index]] += 1 

    def count(self, total: int) -> int:
        result = 0
        for n in self.nums1:
            target = total - n 
            if target in self.counter:
                result += self.counter[target]
        return result 
