# def unique_in_order(sequence):
#     if not sequence:
#         return []
#     res = []
#     for i in range(len(sequence)-1):
#         if sequence[i] != sequence[i+1]:
#             res.append(sequence[i])
#     if not res or sequence[-1] != res[-1]:
#         res.append(sequence[-1])
#     return res

def unique_in_order(iter):
    res = []
    prev = None
    for char in iter:
        if char != prev:
            res.append(char)
            prev = char
    return res

