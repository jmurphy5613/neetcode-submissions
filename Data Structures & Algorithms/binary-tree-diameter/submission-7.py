# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    largestVal = 0
    def search(self, root):
        if not root:
            return 0
        left = self.search(root.left)
        right = self.search(root.right)
        cur =  left + right 
        self.largestVal = max(cur, self.largestVal)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.search(root)
        return self.largestVal
        
