class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head 
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev, curr = None, slow 
        while curr:
            curr.next, prev, curr = prev, curr, curr.next 

        max_sum = 0 
        while prev:
            max_sum = max(max_sum, head.val + prev.val)
            head, prev = head.next, prev.next 

        return max_sum 
