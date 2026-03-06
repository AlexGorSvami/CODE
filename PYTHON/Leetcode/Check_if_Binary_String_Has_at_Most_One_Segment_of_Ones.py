def checkOnesSegment(s: str):
    from collections import Counter
    dic = dict(Counter(s))
    return '1' * dic['1'] in s
