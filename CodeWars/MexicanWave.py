def wave(people):
    res = []
    for i in range(len(people)):
        if people[i].isalpha():
            val = people[:i] + people[i].upper() + people[i+1:]
            res.append(val)
    return res
