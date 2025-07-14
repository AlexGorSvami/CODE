def getDecimalValue(head: Optional[ListNode]) -> int:
    result = 0
    while head is not None:
        result = result << 1 | head.val 
        head = head.next
    return result 
