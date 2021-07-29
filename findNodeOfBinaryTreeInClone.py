# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        stack = [cloned]
        visitedNodes = {}
        while stack:
            curr = stack.pop()
            if curr is None:
                continue
            if curr.val == target.val:
                return curr
            if visitedNodes.get(curr.left) is None:
                stack.append(curr.left)
            if visitedNodes.get(curr.right) is None:
                stack.append(curr.right)
            visitedNodes[curr] = True