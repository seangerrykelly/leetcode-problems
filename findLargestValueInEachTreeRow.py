# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/?envType=daily-question&envId=2024-12-25
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        stack = [(root, 0)]
        rowMap = {}

        while stack:
            node, row = stack.pop()
            if node is None:
                continue
            if row not in rowMap or node.val > rowMap[row]:
                rowMap[row] = node.val
            stack.append((node.left, row + 1))
            stack.append((node.right, row + 1))

        largestValues = rowMap.values()

        return largestValues