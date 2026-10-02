# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    count = 0

    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, maxVal):
            if not root:
                return
            if root.val >= maxVal:
                self.count += 1
            dfs(root.left, max(root.val, maxVal))
            dfs(root.right, max(root.val, maxVal))
        dfs(root, -101)
        return self.count
        
