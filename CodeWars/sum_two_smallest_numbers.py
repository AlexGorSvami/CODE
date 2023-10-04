def sum_two_smallest_numbers(numbers):
    small = min(numbers)
    numbers.remove(small)
    return small + min(numbers)

print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))

