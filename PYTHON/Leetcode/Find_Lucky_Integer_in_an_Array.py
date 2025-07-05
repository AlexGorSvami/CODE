def findLucky(self, arr: List[int]) -> int:
        largest = 0
        for i in arr:
            if i == arr.count(i):
                if i > largest:
                    largest = i
        return -1 if largest == 0 else largest
