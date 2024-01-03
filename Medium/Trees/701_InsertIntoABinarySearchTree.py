# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr, temp = root, root
        while(curr!= None):
            temp = curr
            if(curr.val > val):
                curr = curr.left
            else:
                curr = curr.right
        if(temp.val> val):
            temp.left = TreeNode(val)
        else:
            temp.right = TreeNode(val)
        return root