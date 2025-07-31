def subarrayBitwiseORs(arr: list) -> int:
    prefises = set()
    result = set()

    for i in arr:
        prefises = {i | prefix for prefix in prefises} | {i}
        result |= prefises 
    return len(result)
