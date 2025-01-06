def merge_the_tools(string, k):
    len_str = len(string)
    part = len_str // k
    for i in range(0, len_str, k):
        res = ''
        for j in string[i: i+k]:
            if j in res:
                continue
            else:
                res += j
        print(res)
if __name__ == '__main__':
    merge_the_tools(input(), int(input()))

