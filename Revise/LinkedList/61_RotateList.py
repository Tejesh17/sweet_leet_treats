# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(not head or k ==0 ):
            return head
        count = 0
        curr = head 
        while(curr):
            count+=1
            curr = curr.next
        curr = head

        if(k>= count):
            k = k%count
        if(k ==0):
            return head
        back = None
        for _ in range(count - k):
            back = curr
            curr = curr.next
        back.next = None
        newHead = curr
        for _ in range(k-1):
            curr = curr.next
        curr.next = head
        return newHead