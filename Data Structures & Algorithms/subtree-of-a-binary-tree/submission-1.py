# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def isEquivelant(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True;
            elif p and not q:
                return False
            elif not p and q:
                return False
            return p.val == q.val and isEquivelant(p.left, q.left) and isEquivelant(p.right, q.right)
        return isEquivelant(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)