# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        while(head):
            n = head.next
            if(n and n.val == head.val):
                head.next = head.next.next
            else:
                head = head.next
        return res