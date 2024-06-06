# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        nodeVals = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            nodeVals.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
        nodeVals.sort()
        return nodeVals[k-1]
        