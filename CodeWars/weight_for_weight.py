def order_weight(string):
    first = sorted(string.split(' '))
    second = sorted(first, key=foo)
    return ' '.join(second)

def foo(ls):
    return sum([int(i) for i in ls])
