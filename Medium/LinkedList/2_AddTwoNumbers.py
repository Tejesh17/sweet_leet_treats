# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        curr = res
        carryon = 0
        while(l1 or l2 or carryon):
            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0
            s = l1v +l2v + carryon
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            digit = s%10
            if(carryon ==1):
                carryon = 0
            if(s>=10):
                carryon = 1
            local = ListNode(digit)
            res.next = local
            res = res.next

        return curr.next