# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def findSum(root):
            l,r = 0,0
            if(root.left):
                l = findSum(root.left)
            if(root.right):
                r = findSum(root.right)
            if(root.val>=low and root.val<=high):
                return root.val + l + r
            return l+r
        return findSum(root)