# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
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
                if(not lvl%2):
                    res.append(insideres[::-1])
                else:
                    res.append(insideres)
                insideres=[]
            insideres.append(curr.val)
            if(curr.left):
                q.appendleft((curr.left, lvl+1))
            if(curr.right):
                q.appendleft((curr.right, lvl+1))  
        if(len(res) %2):         
            res.append(insideres[::-1])
        else:
            res.append(insideres)
        return res