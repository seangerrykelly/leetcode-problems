# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return False
        
        univalue = root.val
        nodeQueue = [root]
        
        while nodeQueue:
            curr = nodeQueue.pop(0)
            if curr is None:
                continue
            if curr.val != univalue:
                return False
            nodeQueue.append(curr.left)
            nodeQueue.append(curr.right)
        return True