# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        numbers = []
        def dfs(root, s, numbers):
            if not root.left and not root.right:
                numbers.append(s+str(root.val))
            if root.left:
                dfs(root.left, s+str(root.val), numbers)
            if root.right:
                dfs(root.right, s+str(root.val), numbers)
        dfs(root, "", numbers)
        s = 0 
        for i in numbers:
            s+= int(i)
        return s