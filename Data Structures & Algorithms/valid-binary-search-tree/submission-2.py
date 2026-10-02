# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    isValid = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, minimum, maximum):
            if not root:
                return
            if root.val <= minimum or root.val >= maximum:
                self.isValid = False
                return
            dfs(root.left, minimum, root.val)
            dfs(root.right, root.val, maximum)
        dfs(root, float('-inf'), float('inf'))
        return self.isValid

