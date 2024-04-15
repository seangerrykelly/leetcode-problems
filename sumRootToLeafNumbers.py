# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/?envType=daily-question&envId=2024-04-15
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        leafSum = 0
        stack = [(root, "")]
        isRoot = True

        while stack:
            node, ongoingSum = stack.pop()
            if node is None:
                continue
            ongoingSum += str(node.val)
            if node.left is None and node.right is None:
                leafSum += int(ongoingSum)
            else:
                stack.append((node.left, ongoingSum))
                stack.append((node.right, ongoingSum))

        
        return leafSum

        