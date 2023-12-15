# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        start = head
        while(start):
            count+=1
            start = start.next
        start = head
        noFromFront = count-n
        if(noFromFront == 0):
            head = head.next
            return head
        back = start
        for _ in range(noFromFront):
            back = start
            start = start.next
        back.next = start.next
        return head