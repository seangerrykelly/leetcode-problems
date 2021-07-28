# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def visitNode(self, node, isLeft):
        if node is None:
            return

        if isLeft is True and node.left is None and node.right is None:
            self.leftSum += node.val
        
        self.visitNode(node.left, True)
        self.visitNode(node.right, False)
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.leftSum = 0
        isLeft = None
        self.visitNode(root, None)
        return self.leftSum