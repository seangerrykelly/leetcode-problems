# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        stack = [(root, "")]
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        letterMap = {}
        leafStrings = []

        for i in range(len(alphabet)):
            letterMap[i] = alphabet[i]

        while stack:
            node, ongoingLeafString = stack.pop()
            if node is None:
                continue
            leafString = letterMap[node.val] + ongoingLeafString
            if node.left is None and node.right is None:
                leafStrings.append(leafString)
            else:
                stack.append((node.left, leafString))
                stack.append((node.right, leafString))
        
        return min(leafStrings)

        