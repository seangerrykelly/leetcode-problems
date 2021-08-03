# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        elif root.left is None and root.right is None and root.val == targetSum:
            return True
        
        stack = [(root.val,root.val)]
        nodeStack = [root]
        first = True
        
        while nodeStack:
            currSum, currVal = stack.pop()
            currNode = nodeStack.pop()
            if first is not True:
                currSum += currVal
            if currSum == targetSum and currNode.left is None and currNode.right is None:
                return True
            if currNode.left is not None:
                nodeStack.append(currNode.left)
                stack.append((currSum, currNode.left.val))
            if currNode.right is not None:
                nodeStack.append(currNode.right)
                stack.append((currSum, currNode.right.val))
                
            first = False
        return False
        