# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
class Solution(object):
    def dfs(self, root):
        if root is None:
            return 0
        
        stack = [(root, root.val)]
        result = 0

        while stack:
            currNode, currMaxInPath = stack.pop()

            if currNode.val >= currMaxInPath:
                result += 1
                currMaxInPath = currNode.val

            if currNode.left:
                stack.append((currNode.left, currMaxInPath))
            if currNode.right:
                stack.append((currNode.right, currMaxInPath))
        return result

    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        goodNodeCount = self.dfs(root)
        return goodNodeCount