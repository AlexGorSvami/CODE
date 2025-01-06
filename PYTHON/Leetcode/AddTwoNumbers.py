def add_two_numbers(l1:list, l2:list) -> list:
    dum = []
    cur = dum

    carry = 0
    while l1 or l2 or carry:
        r1 = l1.append(value) if l1 else 0
        r2 = l2.append(value) if l2 else 0

        value = r1 + r2 + carry
        carry = value // 10
        value = value % 10
        cur.next = ListNode(val)

        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dum.next

print(add_two_numbers([2,4,3], [5,6,4]))



