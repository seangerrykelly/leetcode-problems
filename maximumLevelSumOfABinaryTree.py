# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        levelSums = {}
        maxLevelSum = 0
        maxLevel = 1
        def checkNode(node, level):
            if node is None:
                return

            # Update map of level sums
            if level not in levelSums:
                levelSums[level] = node.val
            else:
                levelSums[level] += node.val

            # Check remaining nodes
            checkNode(node.left, level + 1)
            checkNode(node.right, level + 1)

        checkNode(root, 1)

        # Check level sums and get max
        for level in levelSums:
            if level == 1:
                maxLevelSum, maxLevel = levelSums[level], level
            elif levelSums[level] > maxLevelSum:
                maxLevelSum = levelSums[level]
                maxLevel = level
        return maxLevel
            