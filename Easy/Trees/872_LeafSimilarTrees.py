# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafA, leafB = [],[]
        def findLeaf(root, ar):
            if(not root):
                return
            if(root.left == None and root.right ==None):
                ar.append(root.val)
            findLeaf(root.left, ar) 
            findLeaf(root.right, ar)
        findLeaf(root1, leafA)
        findLeaf(root2, leafB)
        return leafA == leafB