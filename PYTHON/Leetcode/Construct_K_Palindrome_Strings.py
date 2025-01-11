def canConstruct(s: str, k: int) -> bool:
    from collections import Counter 
    if len(s) < k:
        return False
    odd_letters = sum(1 if freq & 1 else 0 for freq in Counter(s).values())
    return odd_letters <= k

print(canConstruct('annabelle', 2))
print(canConstruct('leetcode', 3))
print(canConstruct('true',4))
