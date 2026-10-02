# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = [root]
        rightVals = []

        while queue:
            for i in range(len(queue)):
                cur = queue.pop(0)
                if i == 0:
                    rightVals.append(cur.val)
                
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)
        return rightVals
