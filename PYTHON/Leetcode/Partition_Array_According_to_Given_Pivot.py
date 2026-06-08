def pivotArray(nums: list, pivot: int) -> list:
    return [x for x in nums if x < pivot] + [x for x in nums if x == pivot] + [x for x in nums if x > pivot]
