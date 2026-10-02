# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    largestVal = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return self.largestVal
        self.largestVal = max(self.diameterOfBinaryTree(root.right), self.diameterOfBinaryTree(root.left), self.maxDepth(root.left) + self.maxDepth(root.right))
        return self.largestVal
