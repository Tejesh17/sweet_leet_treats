# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = start = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        back = None
        while(slow):
            tmp = slow.next
            slow.next = back
            back = slow
            slow = tmp

        while(back and head):
            if(back.val != head.val):
                return False
            back = back.next
            head = head.next
        return True