# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def maxsum(root):
            nonlocal res
            if not root:
                return 0
            left = maxsum(root.left)
            right = maxsum(root.right)
            localsum = root.val + max(left, right)
            if(left <0 and right <0):
                localsum = root.val
            res = max(res, localsum)
            res = max(res, left+right+ root.val)
            return localsum
        maxsum(root)
        return res
            