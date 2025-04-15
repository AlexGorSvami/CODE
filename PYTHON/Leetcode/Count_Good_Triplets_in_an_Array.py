def goodTriplets(nums1: list, nums2: list) -> int:
    from sortedcontainers import SortedList

    n = len(nums1)
    pos_b = [0] * n
    for ind, value in enumerate(nums2):
        pos_b[value] = ind 

    pre_a = []
    sort_list = SortedList()
    for num1 in nums1:
        pre_a.append(sort_list.bisect_left(pos_b[num1]))
        sort_list.add(pos_b[num1])

    suf_a = []
    sort_list.clear()
    for num1 in nums1[::-1]:
        suf_a.append(len(sort_list) - sort_list.bisect_left(pos_b[num1]))
        sort_list.add(pos_b[num1])

    suf_a.reverse()
    answer = 0
    for pre, suf in zip(pre_a, suf_a):
        answer += pre * suf 

    return answer 

