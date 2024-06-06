# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        valMap = {}
        stack = [root]

        while stack:
            node = stack.pop()
            if node is None:
                continue
            if node.val not in valMap:
                valMap[node.val] = 1
            stack.append(node.left)
            stack.append(node.right)

        keys = valMap.keys()
        keys.sort()

        if len(keys) <= 1:
            return -1
        else:
            return keys[1]
        
