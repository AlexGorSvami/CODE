def minimumBoxes(apple: list, capacity: list) -> int:
    total = sum(apple)
    capacity.sort(reverse=True)
    for ind, val in enumerate(capacity):
        if total <= 0:
            return ind 
        total -= val 

    return len(capacity)
