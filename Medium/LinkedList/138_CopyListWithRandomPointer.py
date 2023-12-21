"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        oldToNew = {None:None}
        while(cur):
            copy = Node(cur.val)
            oldToNew[cur] = copy
            cur = cur.next
        
        cur = head
        while(cur):
            copy = oldToNew[cur]
            copy.next = oldToNew[cur.next]
            copy.random = oldToNew[cur.random]
            cur = cur.next
        
        return oldToNew[head]