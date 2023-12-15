# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        start = head
        back = None

        while(start and start.val == val):
            start = start.next
            head = start
            back = start
        
        while(start ):
            if(start.val == val):
                back.next = start.next
            else:
                back = start
            start = start.next
        return head