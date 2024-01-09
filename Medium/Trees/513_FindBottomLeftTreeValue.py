# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = []
        q = deque()
        q.appendleft((root,0))
        i = 0
        insideres = []
        cur = 0
        while(q):
            curr,lvl  = q.pop()
            if(lvl!= cur):
                cur = lvl
                res.append(insideres[0])
                insideres=[]
            insideres.append(curr.val)
            if(curr.left):
                q.appendleft((curr.left, lvl+1))
            if(curr.right):
                q.appendleft((curr.right, lvl+1))
        res.append(insideres[0])
        return res[-1]