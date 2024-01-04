
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def height(root):
            nonlocal res
            hLeft = hRight = 0
            if(root.left):
                hLeft = height(root.left)
            if(root.right):
                hRight = height(root.right)
            res = max(res, hLeft+hRight)
            return max(hLeft, hRight) +1
        height(root)
        return res