# def solution(s):
#     upper = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
#     res = ''
#     for i in s:
#         if i in upper:
#             res += ' '
#         res += i
#     return res
#
#
# def solution(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)


def solution(s):
    import re
    return re.sub(r'([A-Z])', r' \1', s)
