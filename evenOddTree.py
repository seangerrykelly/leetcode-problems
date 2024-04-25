# https://leetcode.com/problems/even-odd-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [(root, 0)]
        levelMap = {}

        while queue:
            node, level = queue.pop(0)
            if node is None:
                continue

            # Update level map
            if level not in levelMap:
                levelMap[level] = {node.val: 1}
            elif node.val in levelMap[level]:
                return False
            else:
                levelMap[level][node.val] = 1

            # Check that value matches the rule for that level
            levelVals = levelMap[level].keys()
            if level % 2 == 0:
                if node.val != max(levelVals) or node.val % 2 == 0:
                    return False
            elif level % 2 != 0:
                if node.val != min(levelVals) or node.val % 2 != 0:
                    return False
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

        return True
