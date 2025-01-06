def average(array: list):
    array = set(array)
    return sum(array) / len(array)

print(average([1, 2, 3, 4]))
