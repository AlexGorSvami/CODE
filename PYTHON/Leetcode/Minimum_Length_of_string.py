def minimumLength(s: str) -> int:
    from collections import defaultdict 
    storage = defaultdict(int)
    for char in s:
        storage[char] += 1
    result = 0
    for value in storage.values():
        if value % 2 == 1:
            result += 1
        else:
            result += 2
    return result

def minimumLength1(s: str) -> int:
    return sum(1 if x % 2 else 2 for x in Counter(s).values())


print(minimumLength('abaacbcbb'))
print(minimumLength('aa'))
