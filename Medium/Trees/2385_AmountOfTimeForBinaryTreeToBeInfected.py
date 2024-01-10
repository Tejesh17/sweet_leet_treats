# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
            graph = {}
            def traverse(root, parent = None):
                if root.val not in graph:
                    graph[root.val] = []
                if(parent):
                    graph[root.val].append(parent)
                if(root.left):
                    graph[root.val].append(root.left.val)
                    traverse(root.left, root.val)
                if(root.right):
                    graph[root.val].append(root.right.val)
                    traverse(root.right, root.val)
            traverse(root)
            seen = set()
            res = 0
            def dfs(root, val):
                nonlocal res
                val+=1 
                res = max(res, val)
                seen.add(root)
                for i in graph[root]:
                    if i not in seen:
                        dfs(i, val)
            dfs(start, -1)
            return res