# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0
        
        def dfs(root, high):
            nonlocal res
            if(root.val>= high):
                res+=1
                high = root.val
            if(root.left):
                dfs(root.left, high)
            if(root.right):
                dfs(root.right, high)
        dfs(root, float('-inf'))
        return res