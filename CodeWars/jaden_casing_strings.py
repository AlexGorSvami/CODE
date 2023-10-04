def to_jaden_case(string):
    res = ''
    for i in string.split():
        res += i.capitalize() + ' '
    return res.strip()
