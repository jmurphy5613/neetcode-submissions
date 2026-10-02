# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        valToReturn = []
        while queue:
            curList = []
            for i in range(len(queue)):
                c = queue.pop(0)
                curList.append(c.val)

                if c.left:
                    queue.append(c.left)
                if c.right:
                    queue.append(c.right)
            valToReturn.append(curList)
        return valToReturn
    
