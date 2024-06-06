# https://leetcode.com/problems/leaf-similar-trees/description/?envType=daily-question&envId=2024-06-06
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getLeafSequence(self, root):
        leafSequence = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            stack.append(node.left)
            stack.append(node.right)
            if node.left is None and node.right is None:
                leafSequence.append(node.val)
        return leafSequence


    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        sequence1 = self.getLeafSequence(root1)
        sequence2 = self.getLeafSequence(root2)
        return sequence1 == sequence2

        