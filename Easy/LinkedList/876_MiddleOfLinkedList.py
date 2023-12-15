# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0 
        start = head
        while(start):
            count+=1
            start = start.next
        
        start = head
        for _ in range(count//2):
            start = start.next
        return start


# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         fast = slow = head
#         while(fast and fast.next):
#             fast = fast.next.next
#             slow= slow.next
#         return slow