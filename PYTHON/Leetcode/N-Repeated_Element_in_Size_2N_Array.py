def repeatedNTimes(nums: list) -> int:
    visited = set()
    for n in nums:
        if n in visited:
            return n 
        else:
            visited.add(n)
