def compareVersion(version1: str, version2: str) -> int:
    from itertools import zip_longest 
    v1 = [int(i) for i in version1.split('.')]
    v2 = [int(i) for i in version2.split('.')]


    for i, j in zip_longest(v1, v2, fillvalue=0):
        if i > j:
            return 1 
        if i < j:
            return -1 
    return 0 
