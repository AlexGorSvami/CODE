def minimumAbsDifference(arr: list) -> list:
    arr.sort()
    min_diff = float('inf')
    result = []
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] < min_diff:
            min_diff = arr[i] - arr[i-1]
            result = []
        if arr[i] - arr[i-1] == min_diff:
            result.append([arr[i-1], arr[i]])
    return result
