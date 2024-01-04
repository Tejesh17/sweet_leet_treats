# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        res = False
        def helper(root,s):
            nonlocal res
            s += root.val
            if ( s == targetSum and root.left == None and root.right == None):
                res = True
            if(root.right):
                helper(root.right, s)
            if(root.left):
                helper(root.left, s)
        helper(root, 0)
        return res