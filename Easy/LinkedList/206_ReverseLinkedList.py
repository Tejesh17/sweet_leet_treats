# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head):
            return head
        p,q = ListNode(), None
        while(head):
            p = head
            head = head.next
            p.next = q
            q=p
        return p