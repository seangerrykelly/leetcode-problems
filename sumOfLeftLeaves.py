# https://leetcode.com/problems/sum-of-left-leaves/?envType=daily-question&envId=2024-04-14
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        leftLeavesSum = 0
        stack = [(root, False)]

        while stack:
            node, isLeft = stack.pop()
            if node is None:
                continue
            if isLeft and node.left is None and node.right is None:
                leftLeavesSum += node.val
            stack.append((node.left, True))
            stack.append((node.right, False))
        
        return leftLeavesSum
        