# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root, h, l):
            nonlocal res
            if not root:
                return 
            res = max(res, max(abs(h-root.val), abs(l-root.val)))
            h = max(h, root.val)
            l = min(l, root.val)
            dfs(root.left, h,l)
            dfs(root.right, h,l)
        dfs(root,root.val,root.val)
        return res