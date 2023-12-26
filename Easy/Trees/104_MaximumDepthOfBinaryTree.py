# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(r,c):
            nonlocal res
            c+=1
            res = max(res,c)
            if(r and r.left):
                dfs(r.left,c)
            if(r and r.right):
                dfs(r.right,c)
        if(root):
            dfs(root, res)
        return res