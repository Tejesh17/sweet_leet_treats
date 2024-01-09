# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order = []
        def inorder(root):
            if not root: 
                return 
            inorder(root.left)
            in_order.append(root.val)
            inorder(root.right)
        inorder(root)
        return in_order[k-1]