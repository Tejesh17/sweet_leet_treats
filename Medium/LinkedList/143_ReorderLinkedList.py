# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
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

        result = ListNode()
        flag = True
        while(r and head):
            if(flag):
                result.next = head
                head = head.next
                flag = not flag
            else:
                result.next = r
                r = r.next
                flag = not flag
            result = result.next
        return result.next
