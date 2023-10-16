def delete_nth(order,max_e):
    res = []
    for i in order:
        if res.count(i) < max_e:
            res.append(i)
    return res
