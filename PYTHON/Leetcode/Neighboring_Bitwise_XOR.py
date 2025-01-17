def doesValidArrayExist(derived: list) -> bool:
    return sum(derived) & 1 == 0

print(doesValidArrayExist([1,1,0]))
print(doesValidArrayExist([1,1]))
print(doesValidArrayExist([1,0]))
