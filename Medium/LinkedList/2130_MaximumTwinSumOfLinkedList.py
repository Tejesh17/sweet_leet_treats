# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse (head):
            back, n = None, None
            while(head):
                n = head.next
                head.next = back
                back = head
                head = n
            return back
        
        fast, slow = head, head
        while(fast and fast.next):
            fast = fast.next.next
            slow= slow.next
        r = reverse(slow)
        res = 0
        while(r):
            res = max(res, r.val + head.val)
            r = r.next
            head = head.next
        return res
