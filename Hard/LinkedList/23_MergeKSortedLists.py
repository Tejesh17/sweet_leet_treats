# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:   
        def mergeTwoLists( list1, list2):
            res = ListNode()
            finalRes = res
            while(list1 and list2):
                if(list1.val > list2.val):
                    res.next = list2
                    list2 = list2.next
                else:
                    res.next = list1
                    list1 = list1.next
                res = res.next
            if(list1):
                res.next = list1
            elif(list2):
                res.next = list2
            return finalRes.next
            
        def merge(lists):
            if(len(lists)> 2):
                mid = len(lists)//2
                L = merge(lists[:mid])
                R = merge(lists[mid:])
                return mergeTwoLists(L,R)
            elif(len(lists) ==2):
                return mergeTwoLists(lists[0], lists[1])
            elif(len(lists) ==1):
                return lists[0]
        return merge(lists)
