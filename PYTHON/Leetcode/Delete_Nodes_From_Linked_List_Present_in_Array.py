def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
    nums = set(nums)
    dummy = ListNode()
    curr = dummy 

    while head:
        if head.val not in nums:
            curr.next = ListNode(head.val)
            curr = curr.next

        head = head.next 
    
    return dummy.next 
